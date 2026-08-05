/* The keyboard the film draws.
 *
 * Geometry and radicals are the shipping ones, copied from the site's own
 * `glide-decoder.js` and `cangjie-data.js` rather than eyeballed, so a stroke
 * animated here crosses exactly the keys it would cross on a phone. The film is
 * a dramatisation of the demo, not an illustration of something adjacent to it.
 */

export const ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm"] as const;

// The physical stagger: each row starts further in than the one above it.
export const ROW_OFFSETS = [0, 0.5, 1.5] as const;

export const RADICALS: Record<string, string> = {
  a: "日", b: "月", c: "金", d: "木", e: "水", f: "火", g: "土", h: "竹",
  i: "戈", j: "十", k: "大", l: "中", m: "一", n: "弓", o: "人", p: "心",
  q: "手", r: "口", s: "尸", t: "廿", u: "山", v: "女", w: "田", x: "難",
  y: "卜", z: "*",
};

export const KEY_WIDTH = 74;
export const KEY_HEIGHT = 92;
export const GAP = 10;

export type Key = {
  letter: string;
  x: number;
  y: number;
  width: number;
  height: number;
};

export const KEYS: Key[] = ROWS.flatMap((row, rowIndex) =>
  [...row].map((letter, column) => ({
    letter,
    x: (column + ROW_OFFSETS[rowIndex]) * (KEY_WIDTH + GAP),
    y: rowIndex * (KEY_HEIGHT + GAP),
    width: KEY_WIDTH,
    height: KEY_HEIGHT,
  }))
);

export const BOARD_WIDTH = 10 * KEY_WIDTH + 9 * GAP;
export const BOARD_HEIGHT = 3 * KEY_HEIGHT + 2 * GAP;

export const centreOf = (letter: string) => {
  const key = KEYS.find((candidate) => candidate.letter === letter)!;
  return { x: key.x + key.width / 2, y: key.y + key.height / 2 };
};

/* The stroke: h → d → a, all on the home row, which is why it necessarily
   crosses g, f and s on the way. The decoder skips those three at a cost of
   1.0 each and spells hda — 香. Verified by scripts/test_glide_decoder.mjs. */
export const STROKE = ["h", "d", "a"];
export const CROSSED = ["h", "g", "f", "d", "s", "a"];
export const INTENDED = new Set(STROKE);

/** `hda` in the shipped table is `香稈`; the rest are prefix matches after it. */
export const CANDIDATES = ["香", "稈", "白", "的", "鳥", "節"];

export const PALETTE = {
  ivory: "#FAF1E0",
  jade: "#5DDAC7",
  lagoon: "#4CB3BE",
  koi: "#FF5136",
  text: "#F7F4EE",
  muted: "#AAB2C2",
  dim: "#7E8798",
  line: "rgba(255,255,255,0.10)",
  lineStrong: "rgba(255,255,255,0.20)",
};

/** Point at `progress` (0..1) along the polyline through the stroke's centres. */
export function pointAlong(progress: number) {
  const points = STROKE.map(centreOf);
  const legs = points.slice(1).map((point, index) => {
    const previous = points[index];
    return Math.hypot(point.x - previous.x, point.y - previous.y);
  });
  const total = legs.reduce((sum, leg) => sum + leg, 0);
  let travelled = progress * total;
  for (let index = 0; index < legs.length; index += 1) {
    if (travelled <= legs[index]) {
      const t = legs[index] === 0 ? 0 : travelled / legs[index];
      return {
        x: points[index].x + (points[index + 1].x - points[index].x) * t,
        y: points[index].y + (points[index + 1].y - points[index].y) * t,
      };
    }
    travelled -= legs[index];
  }
  return points[points.length - 1];
}

/** How far along the stroke each key is first touched, as a 0..1 progress. */
export function crossingProgress(letter: string) {
  const points = STROKE.map(centreOf);
  const target = centreOf(letter);
  const legs = points.slice(1).map((point, index) =>
    Math.hypot(point.x - points[index].x, point.y - points[index].y)
  );
  const total = legs.reduce((sum, leg) => sum + leg, 0);
  let before = 0;
  for (let index = 0; index < legs.length; index += 1) {
    const from = points[index];
    const to = points[index + 1];
    const legLength = legs[index];
    // Project the key centre onto this leg; if it lands inside, that is when
    // the finger passes it.
    const dx = to.x - from.x;
    const dy = to.y - from.y;
    const t = legLength === 0 ? 0 : ((target.x - from.x) * dx + (target.y - from.y) * dy) / (legLength * legLength);
    if (t >= -0.02 && t <= 1.02) {
      const distance = Math.hypot(from.x + dx * t - target.x, from.y + dy * t - target.y);
      if (distance < KEY_HEIGHT * 0.6) return (before + Math.max(0, Math.min(1, t)) * legLength) / total;
    }
    before += legLength;
  }
  return 1;
}
