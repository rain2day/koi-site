"""Turn section data into HTML.

Content strings are plain text and are escaped. A small inline vocabulary is
recognised so that content modules stay readable without embedding raw markup:

    **emphasis**            -> <strong>
    `literal`               -> <code>
    [label](route:privacy/) -> link within the current language
    [label](mailto:…)       -> external link, passed through
    [label](#anchor)        -> in-page link

``route:`` is resolved against the language the document belongs to, so both
content modules write ``route:privacy/`` and neither needs to know its own URL
prefix. ``site:`` resolves against the site root instead, and exists for the
language switch, which is the one link that deliberately leaves its tree.

Anything a content module does not write cannot appear in the output, which is
what keeps the published pages free of trackers and inline script.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from html import escape
from pathlib import Path

INLINE_PATTERN = re.compile(
    r"\*\*(?P<strong>.+?)\*\*"
    r"|`(?P<code>[^`]+)`"
    r"|\[(?P<label>[^\]]+)\]\((?P<href>[^)]+)\)"
)
SVG_VIEWBOX_PATTERN = re.compile(r'viewBox\s*=\s*"([\d.\s-]+)"')


@dataclass(frozen=True)
class RenderContext:
    """Everything a section needs in order to resolve links and assets."""

    site_root: str
    asset_root: Path
    locale_prefix: str = ""
    root_absolute: bool = False

    def _from_root(self, path: str) -> str:
        return f"/{path}" if self.root_absolute else f"{self.site_root}{path}"

    def href(self, target: str) -> str:
        """Resolve a content href into a document-appropriate URL."""
        if target.startswith("route:"):
            return self._from_root(f"{self.locale_prefix}{target[len('route:'):]}")
        if target.startswith("site:"):
            return self._from_root(target[len("site:") :])
        if target.startswith("asset:"):
            return self._from_root(f"assets/{target[len('asset:'):]}")
        return target


def inline(text: str, context: RenderContext) -> str:
    """Escape ``text`` and expand the inline vocabulary."""
    parts: list[str] = []
    cursor = 0
    for match in INLINE_PATTERN.finditer(text):
        parts.append(escape(text[cursor : match.start()]))
        if match.group("strong") is not None:
            parts.append(f"<strong>{escape(match.group('strong'))}</strong>")
        elif match.group("code") is not None:
            parts.append(f"<code>{escape(match.group('code'))}</code>")
        else:
            href = escape(context.href(match.group("href")), quote=True)
            parts.append(f'<a href="{href}">{escape(match.group("label"))}</a>')
        cursor = match.end()
    parts.append(escape(text[cursor:]))
    return "".join(parts)


def _as_list(values: object) -> list:
    """Accept a single string or a sequence of them, uniformly."""
    if values is None:
        return []
    return [values] if isinstance(values, str) else list(values)


def _paragraphs(values: object, context: RenderContext) -> list[str]:
    if values is None:
        return []
    items = [values] if isinstance(values, str) else list(values)
    return [f"<p>{inline(item, context)}</p>" for item in items]


def _bullets(values: object, context: RenderContext, ordered: bool = False) -> list[str]:
    if not values:
        return []
    tag = "ol" if ordered else "ul"
    items = "".join(f"<li>{inline(item, context)}</li>" for item in values)
    return [f'<{tag} class="list">{items}</{tag}>']


def _heading(section: dict, context: RenderContext) -> list[str]:
    heading = section.get("heading")
    if not heading:
        return []
    anchor = section.get("id")
    label = inline(heading, context)
    if not anchor:
        return [f"<h2>{label}</h2>"]
    href = "#" + escape(anchor, quote=True)
    return [f'<h2 id="{escape(anchor, quote=True)}">' f'<a class="anchor" href="{href}">{label}</a></h2>']


def _image_size(context: RenderContext, source: str) -> tuple[int, int]:
    """Read intrinsic dimensions so every image can reserve its own space."""
    path = context.asset_root / source
    if not path.is_file():
        raise FileNotFoundError(f"referenced image is missing: {path}")
    if path.suffix == ".svg":
        match = SVG_VIEWBOX_PATTERN.search(path.read_text(encoding="utf-8"))
        if not match:
            raise ValueError(f"svg without viewBox cannot be sized: {path}")
        _, _, width, height = (float(value) for value in match.group(1).split())
        return round(width), round(height)
    header = path.read_bytes()[:24]
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"unsupported image format: {path}")
    return int.from_bytes(header[16:20], "big"), int.from_bytes(header[20:24], "big")


def _prose(section: dict, context: RenderContext) -> str:
    body = _heading(section, context)
    body += _paragraphs(section.get("body"), context)
    body += _bullets(section.get("bullets"), context)
    body += _paragraphs(section.get("after"), context)
    return f'<section class="prose">{"".join(body)}</section>'


def _cards(section: dict, context: RenderContext) -> str:
    body = _heading(section, context)
    body += _paragraphs(section.get("intro"), context)
    cards = []
    for item in section["items"]:
        card = []
        if item.get("meta"):
            card.append(f'<p class="card-meta">{inline(item["meta"], context)}</p>')
        card.append(f"<h3>{inline(item['title'], context)}</h3>")
        card.extend(_paragraphs(item.get("body"), context))
        card.extend(_bullets(item.get("bullets"), context))
        cards.append(f'<article class="card">{"".join(card)}</article>')
    columns = section.get("columns", 2)
    body.append(f'<div class="grid grid-{columns}">{"".join(cards)}</div>')
    return f'<section class="block">{"".join(body)}</section>'


def _steps(section: dict, context: RenderContext) -> str:
    body = _heading(section, context)
    body += _paragraphs(section.get("intro"), context)
    steps = []
    for index, item in enumerate(section["items"], start=1):
        step = [f'<p class="step-index" aria-hidden="true">{index}</p>']
        step.append(f"<h3>{inline(item['title'], context)}</h3>")
        step.extend(_paragraphs(item.get("body"), context))
        steps.append(f'<li class="step">{"".join(step)}</li>')
    body.append(f'<ol class="steps">{"".join(steps)}</ol>')
    return f'<section class="block">{"".join(body)}</section>'


def _table(section: dict, context: RenderContext) -> str:
    body = _heading(section, context)
    body += _paragraphs(section.get("intro"), context)
    head = "".join(
        f'<th scope="col">{inline(column, context)}</th>' for column in section["columns"]
    )
    rows = []
    for row in section["rows"]:
        first, *rest = row
        cells = f'<th scope="row">{inline(first, context)}</th>'
        cells += "".join(f"<td>{inline(cell, context)}</td>" for cell in rest)
        rows.append(f"<tr>{cells}</tr>")
    caption = ""
    if section.get("caption"):
        caption = f"<caption>{inline(section['caption'], context)}</caption>"
    table = (
        f'<div class="table-scroll"><table>{caption}'
        f"<thead><tr>{head}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>"
    )
    body.append(table)
    return f'<section class="block">{"".join(body)}</section>'


def _faq(section: dict, context: RenderContext) -> str:
    body = _heading(section, context)
    body += _paragraphs(section.get("intro"), context)
    entries = []
    for item in section["items"]:
        answer = "".join(_paragraphs(item["answer"], context) + _bullets(item.get("bullets"), context))
        entries.append(
            f'<details class="faq-item"><summary>{inline(item["question"], context)}</summary>'
            f'<div class="faq-answer">{answer}</div></details>'
        )
    body.append(f'<div class="faq">{"".join(entries)}</div>')
    return f'<section class="block">{"".join(body)}</section>'


def _definitions(section: dict, context: RenderContext) -> str:
    body = _heading(section, context)
    body += _paragraphs(section.get("intro"), context)
    rows = "".join(
        f"<div class=\"definition\"><dt>{inline(item['term'], context)}</dt>"
        f"<dd>{inline(item['detail'], context)}</dd></div>"
        for item in section["items"]
    )
    body.append(f'<dl class="definitions">{rows}</dl>')
    return f'<section class="block">{"".join(body)}</section>'


def _showcase(section: dict, context: RenderContext) -> str:
    body = _heading(section, context)
    body += _paragraphs(section.get("intro"), context)
    figures = []
    for item in section["items"]:
        width, height = _image_size(context, item["source"])
        source = escape(context.href("asset:" + item["source"]), quote=True)
        classes = "device" if item.get("frame", True) else "plain-shot"
        badge = ""
        if item.get("badge"):
            badge = f'<p class="shot-badge">{inline(item["badge"], context)}</p>'
        figures.append(
            f'<figure class="shot">{badge}'
            f'<div class="{classes}"><img src="{source}" alt="{escape(item["alt"], quote=True)}"'
            f' width="{width}" height="{height}" loading="lazy" decoding="async"></div>'
            f'<figcaption>{inline(item["caption"], context)}</figcaption></figure>'
        )
    body.append(f'<div class="shots">{"".join(figures)}</div>')
    return f'<section class="block">{"".join(body)}</section>'


def _demo(section: dict, context: RenderContext) -> str:
    """The live Cangjie keyboard.

    What renders here is the fallback: the codes worth trying, written out so
    the section still teaches something without JavaScript, on a slow link, or
    to a crawler. The demo module replaces the mount's contents on load, so the
    fallback is never shown twice and never has to be hidden by script.
    """
    body = _heading(section, context)
    body += _paragraphs(section.get("intro"), context)

    tries = "".join(
        f'<li><code>{escape(item["code"])}</code>'
        f'<span class="try-arrow" aria-hidden="true">→</span>'
        f'<span class="try-result">{escape(item["result"])}</span></li>'
        for item in section.get("tries", ())
    )
    prompts = (
        f'<div class="demo-prompts"><p class="demo-prompts-label">'
        f'{inline(section["tries_label"], context)}</p>'
        f'<ul class="try-list">{tries}</ul></div>'
        if tries
        else ""
    )

    fallback = "".join(_paragraphs(section.get("fallback"), context))
    mount = (
        f'<div class="kbd-mount" data-cangjie-demo>'
        f'<div class="kbd-fallback">{fallback}</div></div>'
    )

    body.append(f'<div class="demo">{mount}{prompts}</div>')
    body += _paragraphs(section.get("note"), context)
    return f'<section class="block demo-block">{"".join(body)}</section>'


def _callout(section: dict, context: RenderContext) -> str:
    tone = section.get("tone", "note")
    body = []
    if section.get("heading"):
        body.append(f"<h2>{inline(section['heading'], context)}</h2>")
    body += _paragraphs(section.get("body"), context)
    body += _bullets(section.get("bullets"), context)
    return f'<section class="callout callout-{tone}">{"".join(body)}</section>'


def _scene(section: dict, context: RenderContext) -> str:
    """One beat of the landing page.

    The page used to be eleven stacked card grids: accurate, and a catalogue.
    A scene carries one idea — a numbered statement, a sentence that earns it,
    and at most a few supporting notes — and gives it enough room and type size
    to land before the next one starts. Detail that a reader looks things up in
    rather than reads through belongs on the support page, not here.
    """
    index = section.get("index")
    parts = []
    if index:
        parts.append(f'<p class="scene-index" aria-hidden="true">{escape(index)}</p>')
    if section.get("eyebrow"):
        parts.append(f'<p class="eyebrow">{inline(section["eyebrow"], context)}</p>')

    heading = section["heading"]
    anchor = section.get("id")
    if anchor:
        parts.append(f'<h2 id="{escape(anchor, quote=True)}">{inline(heading, context)}</h2>')
    else:
        parts.append(f"<h2>{inline(heading, context)}</h2>")

    parts += [f'<p class="scene-lead">{inline(line, context)}</p>' for line in _as_list(section.get("lead"))]

    points = section.get("points")
    if points:
        rendered = "".join(
            f'<li><span class="point-title">{inline(point["title"], context)}</span>'
            f'<span class="point-body">{inline(point["body"], context)}</span></li>'
            for point in points
        )
        parts.append(f'<ul class="scene-points">{rendered}</ul>')

    if section.get("aside"):
        parts.append(f'<p class="scene-aside">{inline(section["aside"], context)}</p>')

    tone = section.get("tone", "plain")
    return f'<section class="scene scene-{tone}"><div class="scene-inner">{"".join(parts)}</div></section>'


def _ink(section: dict, context: RenderContext) -> str:
    """A panel you can write on.

    KOI renders its handwriting area as a water surface. This is the closest the
    web can honestly get: the ink is the keyboard's own glide trail and the
    strokes disturb the pond behind the page. Recognition is not here and the
    copy says so — that model runs on the device.
    """
    parts = _heading(section, context)
    parts += _paragraphs(section.get("intro"), context)
    parts.append(
        f'<div class="ink"><canvas class="ink-surface" data-koi-ink '
        f'aria-label="{escape(section["canvas_label"], quote=True)}" role="img"></canvas>'
        f'<p class="ink-hint">{inline(section["hint"], context)}</p></div>'
    )
    parts += _paragraphs(section.get("note"), context)
    return f'<section class="block ink-block">{"".join(parts)}</section>'


RENDERERS = {
    "prose": _prose,
    "cards": _cards,
    "steps": _steps,
    "table": _table,
    "faq": _faq,
    "definitions": _definitions,
    "showcase": _showcase,
    "callout": _callout,
    "demo": _demo,
    "scene": _scene,
    "ink": _ink,
}


def render_sections(sections: list[dict], context: RenderContext) -> str:
    rendered = []
    for section in sections:
        kind = section["kind"]
        if kind not in RENDERERS:
            raise KeyError(f"unknown section kind: {kind}")
        rendered.append(RENDERERS[kind](section, context))
    return "".join(rendered)


def render_contents(sections: list[dict], label: str, context: RenderContext) -> str:
    """Build an in-page table of contents from every anchored section."""
    entries = [
        f'<li><a href="#{escape(section["id"], quote=True)}">{inline(section["heading"], context)}</a></li>'
        for section in sections
        if section.get("id") and section.get("heading")
    ]
    if not entries:
        return ""
    return (
        f'<nav class="contents" aria-label="{escape(label, quote=True)}">'
        f"<h2>{escape(label)}</h2><ol>{''.join(entries)}</ol></nav>"
    )
