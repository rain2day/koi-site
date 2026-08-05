#!/usr/bin/env python3
"""Deploy gate for the KOI public website.

Runs in GitHub Actions (``.github/workflows/pages.yml``) as
``python3 scripts/verify_site.py .`` before the Pages artifact is assembled.
It enforces the production contract for the rendered, bilingual static site:
the exact set of documents and their ``<html lang>`` / canonical / hreflang /
Content-Security-Policy metadata, the privacy-first script and
forbidden-substring policy, that every internal link uses the addressing
scheme its document requires, that every link/stylesheet/icon/image resolves
to a file that actually exists, and the sitemap/robots contract. Standard
library only. Any violation raises a clear message naming the offending file
and value, and the process exits non-zero.
"""

from __future__ import annotations

from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
import xml.etree.ElementTree as ET

ORIGIN = "https://koi.rainsday.com"
ROUTES = ("", "privacy/", "support/", "terms/")
LOCALES = (("zh-Hant", ""), ("en", "en/"))  # (html lang, path prefix)
FORBIDDEN = ("http://", "google-analytics", "googletagmanager", "<iframe", "<form")
ALLOWED_SCRIPT_TYPE = "application/ld+json"
# Vendored third-party libraries. Exempt from the network-API scan only; see
# check_module_sources for why that is safe and what still applies to them.
VENDOR_PREFIX = "assets/vendor/"

# The site runs one first-party script: the Cangjie typing demo. That is a
# deliberate exception to "no JavaScript", and it is only safe because the
# exception is narrow and checked rather than assumed:
#
#   * inline <script> is still limited to JSON-LD, so no logic can be smuggled
#     into a page body;
#   * an executable <script> must be type="module" with a src resolving to a
#     file in this repository, so nothing is ever fetched from another host;
#   * the script files themselves are scanned for the APIs that could reach the
#     network or persist a visitor identifier.
#
# The landing page tells visitors the demo runs entirely on their device. These
# checks are what make that a fact about the artifact rather than a promise.
NETWORK_APIS = (
    "fetch(",
    "XMLHttpRequest",
    "WebSocket",
    "sendBeacon",
    "EventSource",
    "navigator.geolocation",
    "localStorage",
    "sessionStorage",
    "document.cookie",
    "indexedDB",
)
# No standard HTML attribute outside the event-handler family begins with
# "on", so the prefix alone is a sound test for inline script.
INLINE_HANDLER_PREFIX = "on"


@dataclass(frozen=True)
class DocumentSpec:
    """One document the production contract requires to exist."""

    path: str
    lang: str
    prefix: str | None  # None for 404.html
    route: str | None  # None for 404.html
    canonical: str
    root_absolute: bool  # True only for 404.html: it must link with root-absolute paths


def _build_documents() -> list[DocumentSpec]:
    documents = []
    for lang, prefix in LOCALES:
        for route in ROUTES:
            documents.append(
                DocumentSpec(
                    path=f"{prefix}{route}index.html",
                    lang=lang,
                    prefix=prefix,
                    route=route,
                    canonical=f"{ORIGIN}/{prefix}{route}",
                    root_absolute=False,
                )
            )
    documents.append(
        DocumentSpec(
            path="404.html",
            lang="zh-Hant",
            prefix=None,
            route=None,
            canonical=f"{ORIGIN}/404.html",
            root_absolute=True,
        )
    )
    return documents


DOCUMENTS = _build_documents()
OTHER_PREFIX = {"": "en/", "en/": ""}


class PageParser(HTMLParser):
    """Collects every fact ``verify()`` needs from one rendered document."""

    def __init__(self) -> None:
        super().__init__()
        self.lang: str | None = None
        self.canonical: str | None = None
        self.csp: str | None = None
        self.stylesheets: set[str] = set()
        self.icons: set[str] = set()
        self.hreflang: dict[str, str | None] = {}
        self.anchors: set[str] = set()
        self.images: list[dict[str, str | None]] = []
        self.ids: set[str] = set()
        self.scripts: list[dict[str, str | None]] = []
        self.inline_handlers: set[str] = set()
        self.og: dict[str, str | None] = {}
        self.main_count = 0
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)
        for name in values:
            if name.startswith(INLINE_HANDLER_PREFIX):
                self.inline_handlers.add(f"<{tag} {name}>")
        if tag == "html":
            self.lang = values.get("lang")
        elif tag == "link":
            rel = values.get("rel")
            href = values.get("href")
            if rel == "canonical":
                self.canonical = href
            elif rel == "stylesheet" and href is not None:
                self.stylesheets.add(href)
            elif rel in ("icon", "apple-touch-icon") and href is not None:
                self.icons.add(href)
            elif rel == "alternate" and values.get("hreflang") is not None:
                self.hreflang[values["hreflang"]] = href
        elif tag == "a":
            href = values.get("href")
            if href is not None:
                self.anchors.add(href)
        elif tag == "img":
            self.images.append(
                {
                    "src": values.get("src"),
                    "width": values.get("width"),
                    "height": values.get("height"),
                    "alt": values.get("alt"),
                    "aria_hidden": values.get("aria-hidden"),
                }
            )
        elif tag == "script":
            self.scripts.append({"type": values.get("type"), "src": values.get("src")})
        elif tag == "meta":
            prop = values.get("property")
            if prop and prop.startswith("og:"):
                self.og[prop] = values.get("content")
            if (values.get("http-equiv") or "").lower() == "content-security-policy":
                self.csp = values.get("content")
        elif tag == "main":
            self.main_count += 1
        elif tag == "h1":
            self.h1_count += 1


def classify_href(href: str) -> str:
    """Categorise a href so the internal-link rules only apply where they should."""
    if href.startswith("#"):
        return "fragment"
    if href.startswith(("https://", "http://", "mailto:")):
        return "external"
    return "internal"


def resolve_relative_reference(document_path: str, reference: str) -> str:
    """Resolve a same-site href to the repo-relative file it points at.

    Handles both addressing schemes the site uses: paths relative to the
    document's own directory (the 8 localised documents) and root-absolute
    paths (404.html, which GitHub Pages serves for arbitrarily deep missing
    paths). Any ``#fragment`` suffix is stripped first, and a trailing ``/``
    (or a reference that normalises to a directory) maps to ``index.html``.
    """
    path_part = reference.split("#", 1)[0]
    if path_part.startswith("/"):
        trimmed = path_part[1:]
        base = PurePosixPath(".")
        wants_index = path_part.endswith("/") or trimmed in {"", ".", ".."}
    else:
        trimmed = path_part
        base = PurePosixPath(document_path).parent
        wants_index = path_part.endswith("/") or path_part in {"", ".", ".."}
    resolved = PurePosixPath(posixpath.normpath(str(base / trimmed))) if trimmed else base
    if wants_index:
        resolved /= "index.html"
    return str(resolved)


def check(condition: bool, path: str, message: str) -> None:
    """Raise a clear, file-and-value-scoped AssertionError when a check fails."""
    if not condition:
        raise AssertionError(f"{path}: {message}")


def check_forbidden_substrings(path: str, source: str) -> None:
    lowered = source.lower()
    for token in FORBIDDEN:
        check(token not in lowered, path, f"forbidden substring found: {token!r}")


def check_script_policy(root: Path, doc: DocumentSpec, scripts: list[dict[str, str | None]]) -> set[str]:
    """Permit JSON-LD and first-party ES modules; reject everything else.

    Returns the repo-relative paths of the module files this document loads, so
    the caller can scan the sources themselves.
    """
    modules: set[str] = set()
    for script in scripts:
        script_type = script["type"]
        src = script["src"]

        if src is None:
            check(
                script_type == ALLOWED_SCRIPT_TYPE,
                doc.path,
                f"inline <script> with type {script_type!r}; inline script is limited to "
                f"{ALLOWED_SCRIPT_TYPE!r}",
            )
            continue

        check(
            script_type == "module",
            doc.path,
            f'<script src={src!r}> must be type="module", found {script_type!r}',
        )
        check(
            classify_href(src) == "internal",
            doc.path,
            f"<script src={src!r}> must be a first-party path; the site loads no remote script",
        )
        check_reference(root, doc, src, "script src", enforce_style=True)
        modules.add(resolve_relative_reference(doc.path, src))
    return modules


def check_inline_handlers(path: str, handlers: set[str]) -> None:
    for handler in sorted(handlers):
        check(False, path, f"inline event handler {handler} is not permitted")


def check_module_sources(root: Path, modules: set[str]) -> None:
    """Scan shipped JavaScript for anything that could leave the device.

    The site tells visitors the typing demo runs entirely in their browser. This
    is the check that keeps that sentence true as the code changes: a module
    that grows a fetch call, or starts writing localStorage, fails the deploy.

    Both static and dynamic imports are followed, so a helper module cannot dodge
    the scan by not being referenced from HTML directly. Dynamic imports matter
    here specifically: the pond is loaded with ``import()`` so that a visitor who
    cannot use it never downloads it, and following only static imports would
    have left the whole graph behind that call unscanned.

    Vendored third-party code is exempt from the API scan, and only from that.
    A minified library carries loader paths its consumer never calls, so the
    substring scan reports things that cannot happen — three.core.min.js
    contains one ``fetch(`` in code this site does not reach. The guarantee is
    not weakened by the exemption, because it does not rest on this scan: every
    page ships ``connect-src 'none'``, which the browser enforces against all
    code on the page, reachable or not. The exemption is narrow on purpose: the
    file must still exist, must still be same-origin and relative, and must
    still be free of insecure URLs.
    """
    pending = list(modules)
    scanned: set[str] = set()
    while pending:
        module = pending.pop()
        if module in scanned:
            continue
        scanned.add(module)

        path = root / module
        check(path.is_file(), module, "script referenced but missing")
        source = path.read_text(encoding="utf-8")

        if not module.startswith(VENDOR_PREFIX):
            for api in NETWORK_APIS:
                check(
                    api not in source,
                    module,
                    f"uses {api!r}; the demo must not reach the network or persist visitor state",
                )
        check("http://" not in source, module, "contains an insecure http:// URL")

        static = re.finditer(
            r"""^\s*(?:import|export)\b[^;\n]*?from\s+["']([^"']+)["']""", source, re.M
        )
        dynamic = re.finditer(r"""\bimport\s*\(\s*["']([^"']+)["']\s*\)""", source)
        for match in (*static, *dynamic):
            target = match.group(1)
            check(
                target.startswith("."),
                module,
                f"imports {target!r}; only relative first-party imports are permitted",
            )
            pending.append(resolve_relative_reference(module, target))


def check_hreflang(doc: DocumentSpec, hreflang: dict[str, str | None]) -> None:
    if doc.route is None:
        check(not hreflang, doc.path, f"404.html must declare no hreflang links, found {hreflang}")
        return
    zh_canonical = f"{ORIGIN}/{doc.route}"
    en_canonical = f"{ORIGIN}/en/{doc.route}"
    expected = {"zh-Hant": zh_canonical, "en": en_canonical, "x-default": zh_canonical}
    check(hreflang == expected, doc.path, f"hreflang links expected {expected}, found {hreflang}")


def check_csp(path: str, csp: str | None) -> None:
    """Every document must carry a CSP that blocks outbound connections.

    The site's central claim is that it never phones home. A meta-tag CSP
    turns that from a property of our source scanning into something the
    browser itself refuses to violate, regardless of what a future script
    change tries to do.
    """
    check(csp is not None, path, 'missing <meta http-equiv="Content-Security-Policy"> tag')
    check(
        "connect-src 'none'" in csp,
        path,
        f"Content-Security-Policy must include connect-src 'none', found {csp!r}",
    )


def check_open_graph(root: Path, doc: DocumentSpec, og: dict[str, str | None]) -> None:
    for prop in ("og:title", "og:description", "og:url", "og:image"):
        check(bool(og.get(prop)), doc.path, f'missing or empty meta property="{prop}"')
    image = og["og:image"] or ""
    check(image.startswith(f"{ORIGIN}/"), doc.path, f"og:image must be a URL under {ORIGIN}, found {image!r}")
    image_local = image[len(ORIGIN) + 1 :]
    check(image_local.startswith("assets/"), doc.path, f"og:image must live under assets/, found {image!r}")
    check((root / image_local).is_file(), doc.path, f"og:image file does not exist: {image_local}")


def check_images(path: str, images: list[dict[str, str | None]]) -> None:
    for image in images:
        src = image["src"]
        label = f"<img src={src!r}>"
        check(src is not None, path, "<img> missing src attribute")
        check(image["width"] is not None, path, f"{label} missing width attribute")
        check(image["height"] is not None, path, f"{label} missing height attribute")
        alt = image["alt"]
        check(alt is not None, path, f"{label} missing alt attribute")
        if alt == "":
            check(
                image["aria_hidden"] == "true",
                path,
                f'{label} has empty alt but is not aria-hidden="true" '
                "(empty alt is only allowed for decorative images)",
            )


def check_fragment_links(path: str, anchors: set[str], ids: set[str]) -> None:
    for href in anchors:
        if classify_href(href) == "fragment":
            anchor = href[1:]
            check(anchor in ids, path, f"fragment link {href!r} has no matching id in the document")


def check_reference(root: Path, doc: DocumentSpec, href: str, label: str, enforce_style: bool) -> None:
    """Check one same-site href's addressing style and that it resolves to a real file."""
    if classify_href(href) != "internal":
        return
    if enforce_style:
        starts_absolute = href.startswith("/")
        if doc.root_absolute:
            check(
                starts_absolute,
                doc.path,
                f"{label} {href!r} must start with '/' (404.html is served for arbitrarily deep paths)",
            )
        else:
            check(not starts_absolute, doc.path, f"{label} {href!r} must be relative (must not start with '/')")
    target = resolve_relative_reference(doc.path, href)
    check((root / target).is_file(), doc.path, f"{label} {href!r} resolves to missing file {target!r}")


def check_navigation(doc: DocumentSpec, anchors: set[str]) -> None:
    """Every localised document links to all four of its own routes plus its translation."""
    if doc.route is None:
        return
    resolved = {resolve_relative_reference(doc.path, href) for href in anchors if classify_href(href) == "internal"}
    own_routes = {f"{doc.prefix}{route}index.html" for route in ROUTES}
    missing_own = own_routes - resolved
    check(not missing_own, doc.path, f"navigation is missing links to own-language routes: {sorted(missing_own)}")
    other_target = f"{OTHER_PREFIX[doc.prefix]}{doc.route}index.html"
    check(other_target in resolved, doc.path, f"missing link to matching route in other language: {other_target!r}")


def check_sitemap(root: Path) -> None:
    sitemap_path = root / "sitemap.xml"
    check(sitemap_path.is_file(), "sitemap.xml", "file does not exist")
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    tree = ET.parse(sitemap_path)
    locations = {node.text for node in tree.findall(f"{namespace}url/{namespace}loc")}
    expected = {doc.canonical for doc in DOCUMENTS if doc.route is not None}
    check(locations == expected, "sitemap.xml", f"expected canonicals {sorted(expected)}, found {sorted(locations)}")
    check(f"{ORIGIN}/404.html" not in locations, "sitemap.xml", "must not list 404.html")


def check_robots(root: Path) -> None:
    robots_path = root / "robots.txt"
    check(robots_path.is_file(), "robots.txt", "file does not exist")
    content = robots_path.read_text(encoding="utf-8")
    check(f"Sitemap: {ORIGIN}/sitemap.xml" in content, "robots.txt", "missing Sitemap directive")


def verify(root: Path) -> None:
    cname_path = root / "CNAME"
    check(cname_path.is_file(), "CNAME", "file does not exist")
    cname = cname_path.read_text(encoding="utf-8")
    check(cname == "koi.rainsday.com\n", "CNAME", f"expected 'koi.rainsday.com\\n', found {cname!r}")
    check((root / "assets/site.css").is_file(), "assets/site.css", "file does not exist")

    modules: set[str] = set()
    for doc in DOCUMENTS:
        file_path = root / doc.path
        check(file_path.is_file(), doc.path, "document does not exist — run render_site.py first")
        source = file_path.read_text(encoding="utf-8")
        check_forbidden_substrings(doc.path, source)

        parser = PageParser()
        try:
            parser.feed(source)
        except Exception as error:  # html.parser is lenient; stay defensive anyway
            raise AssertionError(f"{doc.path}: failed to parse HTML: {error}") from error

        check(parser.main_count >= 1, doc.path, "missing <main>")
        check(parser.h1_count == 1, doc.path, f"expected exactly one <h1>, found {parser.h1_count}")
        check(parser.lang == doc.lang, doc.path, f"<html lang> expected {doc.lang!r}, found {parser.lang!r}")
        check(
            parser.canonical == doc.canonical,
            doc.path,
            f"canonical expected {doc.canonical!r}, found {parser.canonical!r}",
        )
        check_csp(doc.path, parser.csp)
        modules |= check_script_policy(root, doc, parser.scripts)
        check_inline_handlers(doc.path, parser.inline_handlers)
        check_hreflang(doc, parser.hreflang)
        check_open_graph(root, doc, parser.og)
        check_images(doc.path, parser.images)
        check_fragment_links(doc.path, parser.anchors, parser.ids)

        for href in parser.anchors:
            check_reference(root, doc, href, "link", enforce_style=True)
        for href in parser.stylesheets | parser.icons:
            check_reference(root, doc, href, "stylesheet/icon href", enforce_style=True)
        for image in parser.images:
            src = image["src"]
            if src is not None:
                check_reference(root, doc, src, "image src", enforce_style=True)

        check_navigation(doc, parser.anchors)

    check_module_sources(root, modules)
    check_sitemap(root)
    check_robots(root)


if __name__ == "__main__":
    target = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    try:
        verify(target)
    except AssertionError as error:
        raise SystemExit(f"KOI site verification failed — {error}") from None
    print("KOI site verification passed")
