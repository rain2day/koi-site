/* Tests for the glide decoder against the real demo dictionary.
 *
 * Run: node scripts/test_glide_decoder.mjs
 *
 * The modules under test are plain ES modules with no imports of their own, so
 * they are loaded through data: URLs. That avoids adding a package.json and
 * declaring this static site to be an npm project just to run a test.
 */

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");

async function load(relative) {
  const source = readFileSync(join(root, relative), "utf8");
  return import("data:text/javascript," + encodeURIComponent(source));
}

const { TABLE } = await load("assets/cangjie-data.js");
const glide = await load("assets/glide-decoder.js");

/* ---- dictionary --------------------------------------------------------- */

const CODES = [];
const CHARS = [];
for (const line of TABLE.split("\n")) {
  const space = line.indexOf(" ");
  if (space > 0) {
    CODES.push(line.slice(0, space));
    CHARS.push(line.slice(space + 1));
  }
}
const exact = new Map(CODES.map((code, index) => [code, CHARS[index]]));
const prefixes = new Set();
for (const code of CODES) {
  for (let length = 1; length <= code.length; length += 1) prefixes.add(code.slice(0, length));
}
const isKnown = (code) => prefixes.has(code);
const isExact = (code) => exact.has(code);

/* ---- geometry: a keyboard laid out the way the page lays it out --------- */

const KEY_WIDTH = 34;
const KEY_HEIGHT = 44;
const GAP = 5;
const ROW_INSET = [0, 0.5, 1.5];

const frames = [];
glide.ROWS.forEach((row, rowIndex) => {
  [...row].forEach((letter, column) => {
    frames.push({
      letter,
      x: (column + ROW_INSET[rowIndex]) * (KEY_WIDTH + GAP),
      y: rowIndex * (KEY_HEIGHT + GAP),
      width: KEY_WIDTH,
      height: KEY_HEIGHT,
    });
  });
});
const centre = (letter) => {
  const frame = frames.find((candidate) => candidate.letter === letter);
  return { x: frame.x + frame.width / 2, y: frame.y + frame.height / 2 };
};

/** Drag through the centres of `letters`, sampling densely like a real pointer. */
function stroke(letters) {
  const sampler = glide.createPathSampler(frames);
  const points = letters.map(centre);
  sampler.begin(points[0]);
  for (let index = 1; index < points.length; index += 1) {
    const from = points[index - 1];
    const to = points[index];
    const steps = Math.ceil(Math.hypot(to.x - from.x, to.y - from.y) / 4);
    for (let step = 1; step <= steps; step += 1) {
      const t = step / steps;
      sampler.move({ x: from.x + (to.x - from.x) * t, y: from.y + (to.y - from.y) * t });
    }
  }
  return { segments: sampler.end(), gliding: sampler.isGliding };
}

function candidatesFor(segments) {
  const ranked = glide.decodeGlide(segments, { isKnown, isExact });
  const seen = new Set();
  const out = [];
  for (const entry of ranked) {
    for (const character of exact.get(entry.code) || "") {
      if (!seen.has(character)) {
        seen.add(character);
        out.push(character);
      }
    }
  }
  return { ranked, characters: out };
}

/* ---- tests -------------------------------------------------------------- */

let failures = 0;
const check = (name, condition, detail) => {
  if (condition) {
    console.log(`  pass  ${name}`);
  } else {
    failures += 1;
    console.log(`  FAIL  ${name}${detail ? ` — ${detail}` : ""}`);
  }
};

console.log("glide decoder");

// A straight drag along the home row from h to a passes through g, f, d, s.
// The intended code is hda, so the decoder has to skip g, f and s.
{
  const { segments, gliding } = stroke(["h", "d", "a"]);
  const letters = segments.map((segment) => segment.letter).join("");
  check("a drag across three keys registers as a glide, not a tap", gliding);
  check("intermediate keys are recorded", letters === "hgfdsa", `got "${letters}"`);
  const { ranked, characters } = candidatesFor(segments);
  const top = ranked[0];
  check("hda decodes", ranked.some((entry) => entry.code === "hda"), `top was ${top && top.code}`);
  check("香 is offered", characters.includes("香"), `got ${characters.slice(0, 6).join("")}`);
  const hda = ranked.find((entry) => entry.code === "hda");
  check("skipping three interior keys costs 3.0", hda && Math.abs(hda.penalty - 3.0) < 1e-9,
    hda && `penalty ${hda.penalty}`);
  check("no substitutions were needed", hda && hda.substitutions === 0);
}

// A single press is a tap, and a tap is a literal the decoder may not rewrite.
{
  const sampler = glide.createPathSampler(frames);
  sampler.begin(centre("a"));
  const segments = sampler.end();
  check("a press with no travel stays a tap", segments.length === 1 && segments[0].kind === "tap");
  const { ranked } = candidatesFor(segments);
  check("a tap decodes only to itself", ranked.every((entry) => entry.code === "a"),
    ranked.map((entry) => entry.code).join(","));
}

// Neighbour substitution: nudge the path so it crosses g instead of h.
{
  const { ranked } = candidatesFor([
    { kind: "glide", letter: "g" },
    { kind: "glide", letter: "d" },
    { kind: "glide", letter: "a" },
  ]);
  const hda = ranked.find((entry) => entry.code === "hda");
  check("a clipped neighbour still reaches the intended code", Boolean(hda));
  check("and is charged one substitution at 1.5", hda && hda.substitutions === 1 && hda.penalty === 1.5,
    hda && `subs ${hda.substitutions}, penalty ${hda.penalty}`);
}

// The substitution budget is two, and it is enforced.
{
  const { ranked } = candidatesFor([
    { kind: "glide", letter: "g" },
    { kind: "glide", letter: "s" },
    { kind: "glide", letter: "s" },
  ]);
  check("no decode uses more than two substitutions",
    ranked.every((entry) => entry.substitutions <= glide.MAX_SUBSTITUTIONS));
}

// Turn anchors: you do not change direction on a key by accident, so skipping
// one is expensive.
{
  const anchored = [
    { kind: "glide", letter: "h" },
    { kind: "anchoredGlide", letter: "g" },
    { kind: "glide", letter: "d" },
    { kind: "glide", letter: "a" },
  ];
  const plain = anchored.map((segment) => ({ ...segment, kind: "glide" }));
  const anchoredHda = glide.decodeGlide(anchored, { isKnown, isExact }).find((e) => e.code === "hda");
  const plainHda = glide.decodeGlide(plain, { isKnown, isExact }).find((e) => e.code === "hda");
  check("skipping a turn anchor costs more than skipping a passing key",
    anchoredHda && plainHda && anchoredHda.penalty > plainHda.penalty,
    anchoredHda && plainHda && `${anchoredHda.penalty} vs ${plainHda.penalty}`);
}

// A stroke that turns a corner: e→t→c→u spells 港.
{
  const { segments } = stroke(["e", "t", "c", "u"]);
  const { ranked, characters } = candidatesFor(segments);
  check("a cornering stroke decodes etcu", ranked.some((entry) => entry.code === "etcu"),
    ranked.slice(0, 3).map((entry) => entry.code).join(","));
  check("港 is offered", characters.includes("港"), characters.slice(0, 6).join(""));
}

// A stroke right across the top row is not a word. Cangjie codes are at most
// five radicals, so ten crossings force at least five skips, and the penalty
// ceiling is reached before any of them spells anything. Returning nothing is
// the correct answer: the device falls back to a best-first rescue search here,
// which the demo deliberately does not carry, and inventing a candidate would
// be worse than an empty bar.
{
  const { segments } = stroke(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]);
  const ranked = glide.decodeGlide(segments, { isKnown, isExact });
  check("a meaningless stroke invents nothing", ranked.length === 0, `${ranked.length} results`);
}

// Ceilings hold on a stroke that does decode.
{
  const { segments } = stroke(["h", "g", "f", "d", "s", "a"]);
  const ranked = glide.decodeGlide(segments, { isKnown, isExact });
  check("penalty ceiling holds", ranked.every((entry) => entry.penalty <= glide.MAX_PENALTY));
  check("codes never exceed five radicals",
    ranked.every((entry) => entry.code.length <= glide.MAX_CODE_LENGTH));
}

// Adjacency must be symmetric, or a substitution would work in one direction only.
{
  let symmetric = true;
  for (const [letter, near] of glide.NEIGHBOURS) {
    for (const other of near) {
      if (!(glide.NEIGHBOURS.get(other) || []).includes(letter)) symmetric = false;
    }
  }
  check("neighbour adjacency is symmetric", symmetric);
  check("q neighbours w and a",
    ["w", "a"].every((letter) => glide.NEIGHBOURS.get("q").includes(letter)),
    glide.NEIGHBOURS.get("q").join(""));
}

console.log(failures ? `\n${failures} failing` : "\nAll glide decoder tests passed");
process.exit(failures ? 1 : 0);
