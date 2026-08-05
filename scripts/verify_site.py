#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ORIGIN = "https://koi.rainsday.com"
REQUIRED_HTML = {
    "index.html": f"{ORIGIN}/",
    "privacy/index.html": f"{ORIGIN}/privacy/",
    "support/index.html": f"{ORIGIN}/support/",
    "terms/index.html": f"{ORIGIN}/terms/",
    "404.html": f"{ORIGIN}/404.html",
}
REQUIRED_NAV = {"/", "/privacy/", "/support/", "/terms/"}
FORBIDDEN = ("http://", "google-analytics", "googletagmanager", "<iframe", "<form")


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.canonical: str | None = None
        self.links: set[str] = set()
        self.has_main = False
        self.has_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href")
        if tag == "a" and values.get("href"):
            self.links.add(values["href"] or "")
        self.has_main = self.has_main or tag == "main"
        self.has_h1 = self.has_h1 or tag == "h1"


def verify(root: Path) -> None:
    assert (root / "CNAME").read_text(encoding="utf-8") == "koi.rainsday.com\n"
    assert (root / "assets/site.css").is_file()
    for relative, canonical in REQUIRED_HTML.items():
        source = (root / relative).read_text(encoding="utf-8")
        lowered = source.lower()
        assert all(token not in lowered for token in FORBIDDEN), relative
        parser = PageParser()
        parser.feed(source)
        assert parser.canonical == canonical, (relative, parser.canonical)
        assert parser.has_main and parser.has_h1, relative
        assert REQUIRED_NAV.issubset(parser.links), (relative, parser.links)
    sitemap = ET.parse(root / "sitemap.xml")
    locations = {
        node.text for node in sitemap.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
    }
    assert locations == set(REQUIRED_HTML.values()) - {f"{ORIGIN}/404.html"}
    robots = (root / "robots.txt").read_text(encoding="utf-8")
    assert f"Sitemap: {ORIGIN}/sitemap.xml" in robots


if __name__ == "__main__":
    verify(Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve())
    print("KOI site verification passed")
