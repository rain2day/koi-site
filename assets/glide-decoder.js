/* Glide decoding, ported from KOI's shipping engine.
 *
 * Gliding is the thing the keyboard is actually for: you drag one stroke across
 * the radicals instead of tapping each one, and the decoder works out what you
 * meant even though a finger travelling at speed clips neighbouring keys and
 * misses intended ones. A demo that only accepts taps demonstrates the part
 * every keyboard can already do.
 *
 * The constants below are not invented for the web. They are the values in
 * KOIKeyboardCore (GlidePathSampler.swift, GlideDecoder.swift, KeyPadView.swift),
 * so a stroke that resolves here resolves the same way on the device.
 *
 * Deliberately absent, because the demo dictionary cannot support them
 * honestly: learning-based reranking, the priority-character layer, and the
 * best-first rescue search that runs when the bounded search finds nothing.
 */

/* ---- layout ------------------------------------------------------------- */

export const ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];

// Staggered like the physical keyboard: each row starts half a key further in
// than a naive grid would put it. Neighbour adjacency is computed from these
// offsets rather than from live pixel distance, so it stays stable no matter
// what size the keyboard is rendered at.
const ROW_OFFSETS = [0.0, 0.5, 1.5];

function keyPositions() {
  const positions = new Map();
  ROWS.forEach((row, rowIndex) => {
    [...row].forEach((letter, column) => {
      positions.set(letter, { row: rowIndex, column, centre: column + ROW_OFFSETS[rowIndex] });
    });
  });
  return positions;
}

export const POSITIONS = keyPositions();

/** Physical neighbours: same row one column away, or an adjacent row within one centre-unit. */
export function buildNeighbours() {
  const neighbours = new Map();
  for (const [letter, a] of POSITIONS) {
    const near = [];
    for (const [other, b] of POSITIONS) {
      if (other === letter) continue;
      const sameRow = a.row === b.row && Math.abs(a.column - b.column) === 1;
      const nextRow = Math.abs(a.row - b.row) === 1 && Math.abs(a.centre - b.centre) <= 1.0;
      if (sameRow || nextRow) near.push(other);
    }
    neighbours.set(letter, near);
  }
  return neighbours;
}

export const NEIGHBOURS = buildNeighbours();

/* ---- penalties ---------------------------------------------------------- */

export const PENALTY = {
  interiorSkip: 1.0, //  a clipped key in the middle of the stroke
  edgeSkip: 2.5, //      the first or last crossing: much likelier to be real
  turnAnchorSkip: 8.0, //you do not change direction on a key by accident
  implicitRepeat: 0.8, //one crossing standing in for a doubled radical
  neighbourSubstitution: 1.5,
};

export const MAX_SUBSTITUTIONS = 2;
export const MAX_PENALTY = 6.0;
export const MAX_CODE_LENGTH = 5; // Cangjie never spells a character in more.

/* ---- path sampling ------------------------------------------------------ */

const TOUCH_DOWN_OUTSET = { x: 2, y: 1 };
const GLIDE_OUTSET = { x: 4, y: 6 };
const TURN_MIN_LEG = 7;
const TURN_COSINE = 0.45; // roughly a 63° change of direction

function hit(frames, point, outset) {
  return frames.find(
    (frame) =>
      point.x >= frame.x - outset.x &&
      point.x <= frame.x + frame.width + outset.x &&
      point.y >= frame.y - outset.y &&
      point.y <= frame.y + frame.height + outset.y
  );
}

function contains(frame, point) {
  return (
    point.x >= frame.x &&
    point.x <= frame.x + frame.width &&
    point.y >= frame.y &&
    point.y <= frame.y + frame.height
  );
}

/**
 * Turns a pointer path into the sequence of keys it crossed.
 *
 * `frames` are the on-screen key rectangles in CSS pixels,
 * `[{letter, x, y, width, height}]`.
 */
export function createPathSampler(frames) {
  const minKeyWidth = Math.min(...frames.map((frame) => frame.width));
  const step = Math.max(1, minKeyWidth / 2);
  const activationTravel = Math.max(8, minKeyWidth);

  let initialPoint = null;
  let lastPoint = null;
  let lastKey = null;
  let gliding = false;
  let crossings = []; // {letter, point, anchored}

  function register(letter, point) {
    if (letter === lastKey) return;
    lastKey = letter;
    crossings.push({ letter, point, anchored: false });
    markTurn();
  }

  // A turn is detected at the middle of three consecutive crossings, once both
  // legs are long enough to be a real change of direction rather than jitter.
  function markTurn() {
    if (crossings.length < 3) return;
    const [a, b, c] = crossings.slice(-3);
    const first = { x: b.point.x - a.point.x, y: b.point.y - a.point.y };
    const second = { x: c.point.x - b.point.x, y: c.point.y - b.point.y };
    const firstLength = Math.hypot(first.x, first.y);
    const secondLength = Math.hypot(second.x, second.y);
    if (firstLength < TURN_MIN_LEG || secondLength < TURN_MIN_LEG) return;
    const cosine = (first.x * second.x + first.y * second.y) / (firstLength * secondLength);
    if (cosine < TURN_COSINE) b.anchored = true;
  }

  return {
    begin(point) {
      initialPoint = point;
      lastPoint = point;
      gliding = false;
      crossings = [];
      lastKey = null;
      const frame = hit(frames, point, TOUCH_DOWN_OUTSET);
      if (frame) register(frame.letter, point);
    },

    move(point) {
      if (!lastPoint) return false;
      const distance = Math.hypot(point.x - lastPoint.x, point.y - lastPoint.y);
      const steps = Math.max(1, Math.ceil(distance / step));
      for (let index = 1; index <= steps; index += 1) {
        const t = index / steps;
        const sample = {
          x: lastPoint.x + (point.x - lastPoint.x) * t,
          y: lastPoint.y + (point.y - lastPoint.y) * t,
        };
        // Hysteresis: the key already under the finger keeps the sample as long
        // as the point is still inside its true rect.
        const held = frames.find((frame) => frame.letter === lastKey);
        if (held && contains(held, sample)) continue;
        // A crossing requires actually entering another key. The device widens
        // key rects slightly while gliding, but on the web that produced a real
        // pathology: a diagonal stroke running along the gutter between two rows
        // sits inside both widened rects at once and rattles — one measured
        // stroke produced "e r t f c v g v g h y h y u" for four intended keys,
        // and the spurious crossings ate the whole penalty budget. Requiring
        // true containment makes the sequence deterministic. Forgiveness for
        // clipped keys is the substitution and skip machinery's job, which is
        // where it belongs.
        const frame = frames.find(
          (candidate) => candidate.letter !== lastKey && contains(candidate, sample)
        );
        if (frame) register(frame.letter, sample);
      }
      lastPoint = point;

      if (!gliding) {
        const travel = Math.hypot(point.x - initialPoint.x, point.y - initialPoint.y);
        const foreign = new Set(crossings.slice(1).map((crossing) => crossing.letter));
        gliding = (travel >= activationTravel && foreign.size >= 1) || foreign.size > 1;
      }
      return gliding;
    },

    get isGliding() {
      return gliding;
    },

    /** The crossings as decoder segments. A path that never became a glide is a tap. */
    end() {
      if (!crossings.length) return [];
      if (!gliding) return [{ kind: "tap", letter: crossings[0].letter }];
      return crossings.map((crossing) => ({
        kind: crossing.anchored ? "anchoredGlide" : "glide",
        letter: crossing.letter,
      }));
    },
  };
}

/* ---- decoding ----------------------------------------------------------- */

function skipPenalty(segment, index, count) {
  if (segment.kind === "anchoredGlide") return PENALTY.turnAnchorSkip;
  if (index === 0 || index === count - 1) return PENALTY.edgeSkip;
  return PENALTY.interiorSkip;
}

/**
 * Every code the stroke could plausibly have meant, cheapest first.
 *
 * Depth-first over the crossings. At each one the finger may have meant the key
 * it touched, a neighbour it clipped, nothing at all, or a doubled radical.
 * States are memoised on (segment index, code so far, substitutions used) and a
 * branch is abandoned as soon as a cheaper route to the same state exists, which
 * is what keeps a ten-crossing stroke from exploding combinatorially.
 *
 * `isKnown(code)` reports whether a code exists in the dictionary as an exact
 * entry or as a prefix; it prunes the search and supplies the fit tier.
 */
export function decodeSegments(segments, isKnown) {
  const results = new Map(); // code -> {penalty, substitutions}
  const best = new Map(); // memo key -> cheapest penalty seen
  const count = segments.length;

  function walk(index, code, penalty, substitutions) {
    if (penalty > MAX_PENALTY) return;

    const memoKey = `${index}|${code}|${substitutions}`;
    const seen = best.get(memoKey);
    if (seen !== undefined && seen <= penalty) return;
    best.set(memoKey, penalty);

    if (index === count) {
      if (!code) return;
      const previous = results.get(code);
      if (!previous || penalty < previous.penalty) results.set(code, { penalty, substitutions });
      return;
    }

    const segment = segments[index];

    const extend = (letter, addedPenalty, addedSubstitutions) => {
      if (code.length >= MAX_CODE_LENGTH) return;
      const next = code + letter;
      // Prefix pruning: if no dictionary entry starts with this, every deeper
      // branch is dead too.
      if (!isKnown(next)) return;
      walk(index + 1, next, penalty + addedPenalty, substitutions + addedSubstitutions);
    };

    // A tap is a literal: the user pressed exactly that key and meant it.
    if (segment.kind === "tap") {
      extend(segment.letter, 0, 0);
      return;
    }

    extend(segment.letter, 0, 0);

    if (substitutions < MAX_SUBSTITUTIONS) {
      for (const neighbour of NEIGHBOURS.get(segment.letter) || []) {
        extend(neighbour, PENALTY.neighbourSubstitution, 1);
      }
    }

    // The crossing stands for a doubled radical (the finger cannot cross the
    // same key twice without leaving it).
    if (code.length + 2 <= MAX_CODE_LENGTH) {
      const doubled = code + segment.letter + segment.letter;
      if (isKnown(doubled)) {
        walk(index + 1, doubled, penalty + PENALTY.implicitRepeat, substitutions);
      }
    }

    // The finger clipped this key on its way somewhere else.
    walk(index + 1, code, penalty + skipPenalty(segment, index, count), substitutions);
  }

  walk(0, "", 0, 0);
  return results;
}

/**
 * Decode a stroke into ranked codes.
 *
 * Ordering matches the device: fewest substitutions first, then exact dictionary
 * entries ahead of mere prefixes, then cheapest penalty, then alphabetical so
 * the result is stable.
 */
export function decodeGlide(segments, { isKnown, isExact }) {
  const decoded = decodeSegments(segments, isKnown);
  return [...decoded.entries()]
    .map(([code, score]) => ({
      code,
      penalty: score.penalty,
      substitutions: score.substitutions,
      fitTier: isExact(code) ? 0 : 1,
    }))
    .sort(
      (a, b) =>
        a.substitutions - b.substitutions ||
        a.fitTier - b.fitTier ||
        a.penalty - b.penalty ||
        (a.code < b.code ? -1 : a.code > b.code ? 1 : 0)
    );
}
