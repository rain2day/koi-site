#!/usr/bin/env python3
"""Render the KOI public site from structured content.

Usage: ``python3 scripts/render_site.py``

Traditional Chinese is written to the site root and English to ``/en/``. The two
content modules are checked for structural parity before anything is written, so
a section added to one language and forgotten in the other fails here rather
than reaching production.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from koisite import content_en, content_zh
from koisite.layout import ENGLISH, ORIGIN, ROUTES, TRADITIONAL_CHINESE, render_page

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
LOCALE_CONTENT = ((TRADITIONAL_CHINESE, content_zh), (ENGLISH, content_en))


def section_signature(page: dict) -> list[tuple[str, str | None]]:
    return [(section["kind"], section.get("id")) for section in page["sections"]]


def check_parity() -> None:
    """Both languages must expose the same pages built from the same sections."""
    if set(content_zh.PAGES) != set(content_en.PAGES):
        raise SystemExit(
            f"page sets differ: zh={sorted(content_zh.PAGES)} en={sorted(content_en.PAGES)}"
        )
    if set(content_zh.PAGES) != set(ROUTES):
        raise SystemExit(f"content pages {sorted(content_zh.PAGES)} do not match routes {sorted(ROUTES)}")
    for route in ROUTES:
        chinese = section_signature(content_zh.PAGES[route])
        english = section_signature(content_en.PAGES[route])
        if chinese != english:
            raise SystemExit(
                f"section structure differs for route '/{route}':\n  zh={chinese}\n  en={english}"
            )
    if set(content_zh.UI) != set(content_en.UI):
        raise SystemExit("UI string sets differ between languages")


def write(relative: str, body: str) -> None:
    destination = ROOT / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(body, encoding="utf-8")


def render_sitemap() -> str:
    entries = "".join(
        f"<url><loc>{locale.canonical(route)}</loc></url>"
        for locale, _ in LOCALE_CONTENT
        for route in ROUTES
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{entries}</urlset>\n"
    )


def main() -> None:
    check_parity()
    written = 0
    for locale, content in LOCALE_CONTENT:
        for route in ROUTES:
            document_path = locale.document_path(route)
            write(
                document_path,
                render_page(
                    page=content.PAGES[route],
                    ui=content.UI,
                    locale=locale,
                    route=route,
                    document_path=document_path,
                    asset_root=ASSETS,
                ),
            )
            written += 1

    # 404.html is served for arbitrarily deep missing paths, so it links
    # root-absolutely and is excluded from the sitemap.
    write(
        "404.html",
        render_page(
            page=content_zh.NOT_FOUND,
            ui=content_zh.UI,
            locale=TRADITIONAL_CHINESE,
            route=None,
            document_path="404.html",
            asset_root=ASSETS,
            root_absolute=True,
        ),
    )
    written += 1

    write("sitemap.xml", render_sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}/sitemap.xml\n")
    write("CNAME", "koi.rainsday.com\n")
    print(f"Rendered {written} KOI site pages")


if __name__ == "__main__":
    main()
