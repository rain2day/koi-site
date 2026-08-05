#!/usr/bin/env python3
"""Tests for the deploy gate.

A verifier that passes proves nothing on its own — it has to be shown to fail
on the mistakes it exists to catch. Each case below copies the rendered site,
introduces one defect, and asserts ``verify_site.verify`` rejects it.

Usage: ``python3 scripts/test_verify_site.py``
"""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import verify_site

ROOT = Path(__file__).resolve().parents[1]
COPIED = ("index.html", "404.html", "CNAME", "robots.txt", "sitemap.xml")
COPIED_TREES = ("assets", "privacy", "support", "terms", "en")


def stage(destination: Path) -> None:
    for name in COPIED:
        shutil.copy2(ROOT / name, destination / name)
    for name in COPIED_TREES:
        shutil.copytree(ROOT / name, destination / name)


def edit(root: Path, relative: str, old: str, new: str) -> None:
    path = root / relative
    source = path.read_text(encoding="utf-8")
    if old not in source:
        raise SystemExit(f"test setup failed: {old!r} not found in {relative}")
    path.write_text(source.replace(old, new, 1), encoding="utf-8")


def drop_canonical(root: Path) -> None:
    edit(root, "index.html", 'rel="canonical" href="https://koi.rainsday.com/"',
         'rel="canonical" href="https://koi.rainsday.com/wrong/"')


def inject_tracking_script(root: Path) -> None:
    edit(root, "privacy/index.html", "</head>",
         '<script src="../assets/tracker.js"></script></head>')


def break_hreflang(root: Path) -> None:
    edit(root, "support/index.html", 'hreflang="en" href="https://koi.rainsday.com/en/support/"',
         'hreflang="en" href="https://koi.rainsday.com/en/wrong/"')


def dangling_link(root: Path) -> None:
    edit(root, "terms/index.html", 'href="../privacy/"', 'href="../nowhere/"')


def strip_alt(root: Path) -> None:
    edit(root, "en/index.html", 'alt="" width="256"', 'width="256"')


def absolute_link_in_localised_page(root: Path) -> None:
    edit(root, "index.html", 'href="./privacy/"', 'href="/privacy/"')


def relative_link_in_404(root: Path) -> None:
    edit(root, "404.html", 'href="/privacy/"', 'href="./privacy/"')


def dangling_film_source(root: Path) -> None:
    """A film whose source does not resolve still shows its poster.

    Nothing looks broken — the still frame is there and the play button does
    nothing — so this is exactly the kind of defect a person does not catch.
    """
    edit(root, "index.html", "film/glide.webm", "film/glide-missing.webm")


def api_behind_dynamic_import(root: Path) -> None:
    """A module reachable only through ``import()`` must still be scanned.

    The pond is loaded dynamically so that a visitor who cannot use it never
    downloads it. A gate that followed only static imports would never look at
    it, or at anything it pulls in.
    """
    edit(root, "assets/pond.js", "const MAX_DROPS = 8;",
         "const MAX_DROPS = 8;\nsessionStorage.setItem('seen', '1');")


def insecure_url(root: Path) -> None:
    edit(root, "en/terms/index.html", "https://reportaproblem.apple.com",
         "http://reportaproblem.apple.com")


def second_h1(root: Path) -> None:
    edit(root, "support/index.html", "</main>", "<h1>extra</h1></main>")


def wrong_lang(root: Path) -> None:
    edit(root, "en/privacy/index.html", '<html lang="en">', '<html lang="zh-Hant">')


def dangling_fragment(root: Path) -> None:
    edit(root, "privacy/index.html", 'href="#summary"', 'href="#does-not-exist"')


def shrink_sitemap(root: Path) -> None:
    edit(root, "sitemap.xml", "<url><loc>https://koi.rainsday.com/en/terms/</loc></url>", "")


def sitemap_lists_404(root: Path) -> None:
    edit(root, "sitemap.xml", "</urlset>",
         "<url><loc>https://koi.rainsday.com/404.html</loc></url></urlset>")


def missing_og_image(root: Path) -> None:
    (root / "assets/og-koi.png").unlink()


def wrong_cname(root: Path) -> None:
    (root / "CNAME").write_text("koi.example.com\n", encoding="utf-8")


def missing_document(root: Path) -> None:
    (root / "en/support/index.html").unlink()


def broken_stylesheet(root: Path) -> None:
    edit(root, "index.html", 'href="./assets/site.css"', 'href="./assets/missing.css"')


def embedded_form(root: Path) -> None:
    edit(root, "support/index.html", "</main>", "<form></form></main>")


def loosen_csp(root: Path) -> None:
    edit(root, "index.html", "connect-src 'none'", "connect-src 'self'")


CASES = {
    "canonical must match the route": drop_canonical,
    "only ld+json script tags are allowed": inject_tracking_script,
    "hreflang must point at the real translation": break_hreflang,
    "internal links must resolve to a real file": dangling_link,
    "images must carry alt text": strip_alt,
    "localised pages must link relatively": absolute_link_in_localised_page,
    "404 must link root-absolutely": relative_link_in_404,
    "no plaintext http:// urls": insecure_url,
    "exactly one h1 per document": second_h1,
    "html lang must match the tree": wrong_lang,
    "fragment links must have a matching id": dangling_fragment,
    "sitemap must list every public route": shrink_sitemap,
    "sitemap must not list 404": sitemap_lists_404,
    "og:image file must exist": missing_og_image,
    "CNAME must be the production domain": wrong_cname,
    "every required document must exist": missing_document,
    "stylesheet href must resolve": broken_stylesheet,
    "no embedded forms": embedded_form,
    "CSP connect-src must be 'none'": loosen_csp,
    "modules reached only by dynamic import are scanned": api_behind_dynamic_import,
    "film sources must resolve": dangling_film_source,
}


def main() -> None:
    with tempfile.TemporaryDirectory() as pristine_dir:
        pristine = Path(pristine_dir) / "site"
        pristine.mkdir()
        stage(pristine)

        try:
            verify_site.verify(pristine)
        except AssertionError as error:
            raise SystemExit(f"the unmodified rendered site must pass, but failed: {error}")
        print("  pass  unmodified site is accepted")

        failures = []
        for description, mutate in CASES.items():
            with tempfile.TemporaryDirectory() as case_dir:
                case = Path(case_dir) / "site"
                shutil.copytree(pristine, case)
                mutate(case)
                try:
                    verify_site.verify(case)
                except AssertionError:
                    print(f"  pass  {description}")
                    continue
                except Exception as error:  # a crash is not a controlled rejection
                    failures.append(f"{description} — rejected by crash, not by a check: {error!r}")
                    print(f"  FAIL  {description} (crashed instead of asserting)")
                    continue
                failures.append(f"{description} — the verifier accepted a defective site")
                print(f"  FAIL  {description}")

    if failures:
        raise SystemExit(
            f"\n{len(failures)} gate test(s) failed:\n" + "\n".join(f"  - {item}" for item in failures)
        )
    print(f"\nAll {len(CASES)} deploy-gate tests passed")


if __name__ == "__main__":
    main()
