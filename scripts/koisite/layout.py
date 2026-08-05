"""Document shell: head metadata, navigation, hero, footer.

Traditional Chinese is served from the site root so that the app's
``KOIPublicSiteConfiguration``, which appends ``/privacy/`` and ``/support/`` to
the configured origin, keeps resolving without any client change. English lives
under ``/en/``.

Every internal link is written relative to the document that contains it, so the
site also works when served from a GitHub Pages project path. ``404.html`` is the
one exception: GitHub Pages serves it for arbitrarily deep missing paths, where
relative links would resolve against a directory that does not exist, so that
document uses root-absolute links instead.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from html import escape
from pathlib import PurePosixPath

from .components import RenderContext, inline, render_contents, render_sections

ORIGIN = "https://koi.rainsday.com"
SOURCE_URL = "https://github.com/rain2day/koi-site"
OG_IMAGE = "og-koi.png"
ROUTES = ("", "privacy/", "support/", "terms/")
NAV_KEYS = {"": "nav_home", "privacy/": "nav_privacy", "support/": "nav_support", "terms/": "nav_terms"}


@dataclass(frozen=True)
class Locale:
    code: str
    prefix: str
    og_locale: str

    def route_path(self, route: str) -> str:
        return f"{self.prefix}{route}"

    def document_path(self, route: str) -> str:
        return f"{self.prefix}{route}index.html"

    def canonical(self, route: str) -> str:
        return f"{ORIGIN}/{self.prefix}{route}"


TRADITIONAL_CHINESE = Locale(code="zh-Hant", prefix="", og_locale="zh_HK")
ENGLISH = Locale(code="en", prefix="en/", og_locale="en_US")
LOCALES = (TRADITIONAL_CHINESE, ENGLISH)


def site_root_for(document_path: str) -> str:
    """Relative path from a generated document back to the site root."""
    depth = len(PurePosixPath(document_path).parent.parts)
    return "./" if depth == 0 else "../" * depth


def _structured_data(page: dict, locale: Locale) -> str:
    """Describe the product for search engines. Claims only, no offers."""
    payload = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "KOI Keyboard",
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "iOS 16.0 or later",
        "url": locale.canonical(""),
        "image": f"{ORIGIN}/assets/{OG_IMAGE}",
        "inLanguage": [item.code for item in LOCALES],
        "description": page["description"],
        "author": {"@type": "Person", "name": "RaIN"},
    }
    body = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return f'<script type="application/ld+json">{body}</script>'


def _head(page: dict, locale: Locale, route: str | None, context: RenderContext) -> str:
    title = escape(page["title"], quote=True)
    description = escape(page["description"], quote=True)
    canonical = page.get("canonical") or locale.canonical(route or "")
    stylesheet = escape(context.href("asset:site.css"), quote=True)
    parts = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{title}</title>",
        f'<meta name="description" content="{description}">',
        '<meta name="color-scheme" content="dark">',
        '<meta name="theme-color" content="#07090f">',
        f'<link rel="canonical" href="{escape(canonical, quote=True)}">',
    ]
    if route is not None:
        for other in LOCALES:
            parts.append(
                f'<link rel="alternate" hreflang="{other.code}" href="{escape(other.canonical(route), quote=True)}">'
            )
        parts.append(
            f'<link rel="alternate" hreflang="x-default" '
            f'href="{escape(TRADITIONAL_CHINESE.canonical(route), quote=True)}">'
        )
    parts += [
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{description}">',
        f'<meta property="og:url" content="{escape(canonical, quote=True)}">',
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="KOI Keyboard">',
        f'<meta property="og:locale" content="{locale.og_locale}">',
        f'<meta property="og:image" content="{ORIGIN}/assets/{OG_IMAGE}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<link rel="icon" href="{escape(context.href("asset:koi-mark.png"), quote=True)}" type="image/png">',
        f'<link rel="apple-touch-icon" href="{escape(context.href("asset:koi-mark.png"), quote=True)}">',
        f'<link rel="stylesheet" href="{stylesheet}">',
    ]
    if page.get("structured_data"):
        parts.append(_structured_data(page, locale))
    return "".join(parts)


def _navigation(ui: dict, locale: Locale, route: str | None, context: RenderContext) -> str:
    links = []
    for target in ROUTES:
        label = escape(ui[NAV_KEYS[target]])
        href = escape(context.href(f"site:{locale.route_path(target)}"), quote=True)
        current = ' aria-current="page"' if target == route else ""
        links.append(f'<a href="{href}"{current}>{label}</a>')
    other = ENGLISH if locale is TRADITIONAL_CHINESE else TRADITIONAL_CHINESE
    switch_route = other.route_path(route if route is not None else "")
    switch = (
        f'<a class="lang-switch" lang="{other.code}" hreflang="{other.code}" '
        f'href="{escape(context.href("site:" + switch_route), quote=True)}" '
        f'aria-label="{escape(ui["switch_aria"], quote=True)}">{escape(ui["switch_label"])}</a>'
    )
    brand_href = escape(context.href(f"site:{locale.prefix}"), quote=True)
    mark = escape(context.href("asset:koi-mark.png"), quote=True)
    brand = (
        f'<a class="brand" href="{brand_href}">'
        f'<img src="{mark}" alt="" width="256" height="256" aria-hidden="true">'
        f"<span>KOI</span></a>"
    )
    return (
        f'<header><nav class="shell" aria-label="{escape(ui["nav_label"], quote=True)}">{brand}'
        f'<div class="nav-links">{"".join(links)}{switch}</div></nav></header>'
    )


def _hero(page: dict, context: RenderContext) -> str:
    parts = [f'<p class="eyebrow">{escape(page["eyebrow"])}</p>']
    parts.append(f'<h1>{escape(page["heading"])}</h1>')
    lede = page.get("lede")
    if lede:
        values = [lede] if isinstance(lede, str) else lede
        parts += [f'<p class="lede">{escape(value)}</p>' for value in values]
    status = page.get("status")
    if status:
        parts.append(
            f'<p class="status"><span class="status-dot" aria-hidden="true"></span>'
            f'<span class="status-label">{escape(status["label"])}</span>'
            f'<span class="status-detail">{escape(status["detail"])}</span></p>'
        )
    if page.get("updated"):
        parts.append(f'<p class="updated">{escape(page["updated"])}</p>')
    variant = page.get("hero", "page")
    return f'<div class="hero hero-{variant}">{"".join(parts)}</div>'


def _footer(ui: dict, locale: Locale, context: RenderContext) -> str:
    links = "".join(
        f'<a href="{escape(context.href(f"site:{locale.route_path(target)}"), quote=True)}">'
        f"{escape(ui[NAV_KEYS[target]])}</a>"
        for target in ROUTES
    )
    # The typing demo runs on a dictionary derived from LGPL-3.0 upstream work.
    # Attribution has to be visible on the pages that serve it, not only in the
    # repository, so it renders in the footer of every page.
    notice = ""
    if ui.get("footer_notice"):
        notice = f'<p class="footer-notice">{inline(ui["footer_notice"], context)}</p>'
    return (
        '<footer><div class="shell footer-inner">'
        f'<p class="footer-rights">{escape(ui["footer_rights"])}</p>'
        f'<nav class="footer-links" aria-label="{escape(ui["footer_nav_label"], quote=True)}">{links}</nav>'
        f'<p class="footer-source"><a href="{SOURCE_URL}">{escape(ui["footer_source"])}</a></p>'
        f"{notice}"
        "</div></footer>"
    )


def render_page(
    page: dict,
    ui: dict,
    locale: Locale,
    route: str | None,
    document_path: str,
    asset_root,
    root_absolute: bool = False,
) -> str:
    context = RenderContext(
        site_root=site_root_for(document_path),
        asset_root=asset_root,
        locale_prefix=locale.prefix,
        root_absolute=root_absolute,
    )
    sections = page["sections"]
    body = _hero(page, context)
    if page.get("toc"):
        body += render_contents(sections, ui["contents_label"], context)
    body += render_sections(sections, context)
    skip = f'<a class="skip-link" href="#main">{escape(ui["skip"])}</a>'

    # Modules load at the end of the body and are deferred by definition, so the
    # page paints and is readable before the demo's dictionary is parsed.
    scripts = "".join(
        f'<script type="module" src="{escape(context.href(f"asset:{name}"), quote=True)}"></script>'
        for name in page.get("scripts", ())
    )
    return (
        "<!doctype html>\n"
        f'<html lang="{locale.code}">\n'
        f"<head>{_head(page, locale, route, context)}</head>\n"
        f"<body>{skip}{_navigation(ui, locale, route, context)}"
        f'<main class="shell" id="main">{body}</main>'
        f"{_footer(ui, locale, context)}{scripts}</body>\n</html>\n"
    )
