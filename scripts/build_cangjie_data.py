#!/usr/bin/env python3
"""Build the Cangjie dictionary the site's typing demo runs on.

The demo is a faithful but deliberately reduced copy of the shipping engine: it
carries the characters a visitor would plausibly type, not the 27,584 the app
bundles. Reducing it here rather than in the browser is what keeps the page
fast and the payload honest — nothing is downloaded at runtime.

Sources live in the private application repository and are passed in by path:

    python3 scripts/build_cangjie_data.py \\
        --cin  ../urkeyboard/cangjie35_mobile.cin \\
        --rank ../urkeyboard/ranking-traditional.txt

``cangjie35_mobile.cin`` is the merged Cangjie 3 + 5 table the app ships,
already filtered to the Basic Multilingual Plane because iOS renders
supplementary-plane characters as tofu. ``ranking-traditional.txt`` is Conway's
public-domain commonality ranking (earlier = more common), which decides both
which characters survive and the order candidates appear in.

The output is committed so that GitHub Pages can serve it and so that
regenerating it produces a reviewable diff.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

# Characters ranked beyond this position are dropped. Conway's table ranks
# 3,031 characters, so the default keeps all of them; the flag exists so the
# payload can be trimmed without editing code.
DEFAULT_RANK_LIMIT = 3200

# Apple's Cangjie shows at most this many candidates before the user has to
# page, and the demo bar has no paging control, so anything past it is weight
# the visitor can never reach.
MAX_CANDIDATES_PER_CODE = 12

# The 24 Cangjie radicals in QWERTY order, read from the .cin %keyname block.
KEYNAME_BEGIN = "%keyname begin"
KEYNAME_END = "%keyname end"
CHARDEF_BEGIN = "%chardef begin"
CHARDEF_END = "%chardef end"


def read_ranking(path: Path, limit: int) -> dict[str, int]:
    """Map character -> commonality rank. Earliest appearance wins."""
    ranks: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            continue
        for character in line.strip():
            if character and character not in ranks:
                ranks[character] = len(ranks)
    return {char: rank for char, rank in ranks.items() if rank < limit}


def read_cin(path: Path) -> tuple[dict[str, str], list[tuple[str, str]]]:
    """Return the keyname map and every (code, character) pair, in file order."""
    radicals: dict[str, str] = {}
    entries: list[tuple[str, str]] = []
    section = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == KEYNAME_BEGIN:
            section = "keyname"
            continue
        if stripped == KEYNAME_END:
            section = None
            continue
        if stripped == CHARDEF_BEGIN:
            section = "chardef"
            continue
        if stripped == CHARDEF_END:
            section = None
            continue
        parts = stripped.split()
        if len(parts) != 2:
            continue
        code, value = parts
        if section == "keyname":
            radicals[code] = value
        elif section == "chardef":
            entries.append((code, value))
    if not radicals:
        raise SystemExit(f"{path}: no %keyname block found")
    if not entries:
        raise SystemExit(f"{path}: no %chardef entries found")
    return radicals, entries


def build_table(
    entries: list[tuple[str, str]], ranks: dict[str, int]
) -> dict[str, list[str]]:
    """Group surviving characters by code, preserving the shipping order.

    The .cin is already sorted the way the app ranks candidates — by weight,
    which folds in character frequency and the manual Hong Kong Cantonese
    boost, so code ``r`` leads with 口 and then 吧呢嗎啦. Re-sorting by Conway's
    ranking would throw that away and push the radicals off their own keys, so
    the ranking is used only to decide which characters are common enough to
    ship, never to reorder them.

    Codes containing ``z`` are dropped: they are pre-expanded wildcard rows
    (``izo`` reaching 似), two thirds of the file, and a feature the demo does
    not offer. Keeping them would corrupt prefix matching.

    A character can carry several codes — Cangjie 3 and 5 disagree on some
    decompositions and the shipping table accepts both — and every one is kept,
    because the point of the demo is that either spelling works.
    """
    grouped: dict[str, list[str]] = {}
    for code, character in entries:
        if len(character) != 1 or character not in ranks:
            continue
        code = code.lower()
        if not code.isalpha() or not code.isascii() or "z" in code:
            continue
        bucket = grouped.setdefault(code, [])
        if character not in bucket and len(bucket) < MAX_CANDIDATES_PER_CODE:
            bucket.append(character)
    return grouped


def render_module(radicals: dict[str, str], table: dict[str, list[str]]) -> str:
    """Emit the data as a JS module.

    Codes are emitted sorted and newline-separated rather than as a JSON object
    so the demo can binary-search the code list for a prefix range instead of
    building an index of every prefix at load time.
    """
    lines = [f"{code} {''.join(chars)}" for code, chars in sorted(table.items())]
    payload = "\n".join(lines)
    radical_json = json.dumps(radicals, ensure_ascii=False, sort_keys=True)
    character_count = len({char for chars in table.values() for char in chars})
    return (
        "/* Generated by scripts/build_cangjie_data.py — do not edit by hand.\n"
        f"   {len(table)} codes, {character_count} characters, "
        "derived from the Cangjie 3+5 table the KOI app ships and Conway's\n"
        "   public-domain traditional-character ranking.\n"
        "\n"
        "   This file is a derived work of the following upstream tables:\n"
        "     rime/rime-cangjie          LGPL-3.0-or-later\n"
        "     Arthurmcarthur/Cangjie3-Plus   MIT\n"
        "     stroke-input/stroke-input-data (ranking-traditional.txt)  public domain\n"
        "\n"
        "   It is distributed under LGPL-3.0-or-later, the strongest of those\n"
        "   terms. It is a standalone ES module, separable and replaceable\n"
        "   without modifying the rest of the site, which is what keeps the\n"
        "   remainder of this repository under its own licence. Full notices\n"
        "   and licence texts: THIRD-PARTY.md and licenses/ in this repository. */\n"
        "export const RADICALS = "
        f"{radical_json};\n\n"
        "export const TABLE = `"
        f"{payload}"
        "`;\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cin", required=True, type=Path, help="path to cangjie35_mobile.cin")
    parser.add_argument("--rank", required=True, type=Path, help="path to ranking-traditional.txt")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "assets" / "cangjie-data.js",
    )
    parser.add_argument("--rank-limit", type=int, default=DEFAULT_RANK_LIMIT)
    args = parser.parse_args()

    ranks = read_ranking(args.rank, args.rank_limit)
    radicals, entries = read_cin(args.cin)
    table = build_table(entries, ranks)

    missing = sorted(set(ranks) - {char for chars in table.values() for char in chars})
    args.out.write_text(render_module(radicals, table), encoding="utf-8")

    size_kb = args.out.stat().st_size / 1024
    print(f"wrote {args.out} — {len(table)} codes, {size_kb:.1f} KB")
    if missing:
        print(f"note: {len(missing)} ranked characters have no Cangjie code: {''.join(missing[:40])}")


if __name__ == "__main__":
    main()
