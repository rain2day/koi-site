#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from textwrap import dedent

ORIGIN = "https://koi.rainsday.com"
ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    "index.html": {
        "title": "KOI Keyboard",
        "description": "KOI Keyboard official product website.",
        "canonical": f"{ORIGIN}/",
        "eyebrow": "KOI Keyboard",
        "heading": "為香港文字而設計。",
        "body": dedent("""
            <p class="lede">KOI Keyboard 官方網站基礎已經就緒。產品介紹與完整圖片正在準備中。</p>
            <section class="grid" aria-label="Website sections">
              <article class="card"><h2>Privacy</h2><p>了解 KOI 的私隱政策頁面狀態。</p><a href="/privacy/">查看 Privacy</a></article>
              <article class="card"><h2>Support</h2><p>取得 KOI 支援及聯絡資料。</p><a href="/support/">查看 Support</a></article>
            </section>
            <p class="notice">This is the official technical base for KOI Keyboard. Final product content is being prepared.</p>
        """).strip(),
    },
    "privacy/index.html": {
        "title": "KOI Keyboard Privacy",
        "description": "Privacy information for KOI Keyboard.",
        "canonical": f"{ORIGIN}/privacy/",
        "eyebrow": "KOI · Privacy",
        "heading": "Privacy Policy",
        "body": dedent("""
            <p class="lede">KOI Keyboard 的完整私隱政策正在準備及審閱中。正式版本發佈前，本頁不會作出未經確認的資料處理聲明。</p>
            <section class="card"><h2>Privacy contact</h2><p>私隱查詢：<a href="mailto:privacy@rainsday.com">privacy@rainsday.com</a></p></section>
        """).strip(),
    },
    "support/index.html": {
        "title": "KOI Keyboard Support",
        "description": "Support and contact information for KOI Keyboard.",
        "canonical": f"{ORIGIN}/support/",
        "eyebrow": "KOI · Support",
        "heading": "KOI Support",
        "body": dedent("""
            <p class="lede">KOI Keyboard 的完整支援資料正在準備中。</p>
            <section class="card"><h2>Contact</h2><p>支援查詢：<a href="mailto:support@rainsday.com">support@rainsday.com</a></p><p>私隱查詢：<a href="mailto:privacy@rainsday.com">privacy@rainsday.com</a></p></section>
        """).strip(),
    },
    "terms/index.html": {
        "title": "KOI Keyboard Terms",
        "description": "Terms information for KOI Keyboard.",
        "canonical": f"{ORIGIN}/terms/",
        "eyebrow": "KOI · Terms",
        "heading": "Terms",
        "body": dedent("""
            <p class="lede">KOI 專用條款內容正在準備及審閱中。</p>
            <section class="card"><h2>Subscriptions</h2><p>KOI App 內訂閱目前繼續使用 Apple Standard EULA。此頁不取代 App 內顯示的 Apple 條款連結。</p></section>
        """).strip(),
    },
    "404.html": {
        "title": "KOI Keyboard — Page Not Found",
        "description": "The requested KOI Keyboard page was not found.",
        "canonical": f"{ORIGIN}/404.html",
        "eyebrow": "KOI · 404",
        "heading": "找不到頁面",
        "body": '<p class="lede">你要求的頁面不存在或已經移動。</p><p><a href="/">返回 KOI 首頁</a></p>',
    },
}

TEMPLATE = dedent("""\
    <!doctype html>
    <html lang="zh-Hant">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{title}</title>
      <meta name="description" content="{description}">
      <link rel="canonical" href="{canonical}">
      <meta property="og:title" content="{title}">
      <meta property="og:url" content="{canonical}">
      <meta property="og:type" content="website">
      <link rel="stylesheet" href="/assets/site.css">
    </head>
    <body>
      <header><nav class="shell" aria-label="Primary"><a class="brand" href="/">KOI</a><div class="nav-links"><a href="/">首頁</a><a href="/privacy/">Privacy</a><a href="/support/">Support</a><a href="/terms/">Terms</a></div></nav></header>
      <main class="shell">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{heading}</h1>
        {body}
      </main>
      <footer><div class="shell"><span>© 2026 RaIN</span><span><a href="/privacy/">Privacy</a> · <a href="/support/">Support</a> · <a href="/terms/">Terms</a></span></div></footer>
    </body>
    </html>
""")

for relative, page in PAGES.items():
    destination = ROOT / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(TEMPLATE.format(**page), encoding="utf-8")

print(f"Rendered {len(PAGES)} KOI site pages")
