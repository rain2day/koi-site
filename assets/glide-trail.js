/* Canvas reproduction of the KOI iOS keyboard's glide trail, ported from the
 * shipping Swift source (KeyPadView.swift's rebuildTrailPath and its helpers,
 * KeyButton.swift's KoiTrailPalette) rather than eyeballed from a recording.
 *
 * Self-contained ES module: no imports, no network access of any kind, and
 * no persisted browser state (storage, cookies, or caches). The deploy gate
 * scans every shipped module's raw source for the specific APIs that could
 * reach either, so this file avoids even naming them here in a comment --
 * it stays clean of them on its own merits, not by accident.
 */

// -- timing & shape constants, mirrored 1:1 from KeyPadView's own constants -
const TRAIL_LIFETIME = 0.3; // seconds a sample survives before it is pruned
const EVAPORATION_DURATION = 0.25; // seconds from lift() to a hard clear()
const MAX_HALF_WIDTH = 5.0; // CSS px, ribbon half-width at age 0
const WIDTH_DECAY_EXPONENT = 1.5;
const ARC_MIN_WIDTH = 0.1; // below this the head cap arc is skipped entirely

const PALETTE = {
  ivory: [250, 241, 224], // #FAF1E0
  jade: [93, 218, 199], // #5DDAC7
  lagoon: [76, 179, 190], // #4CB3BE
};

const rgba = ([r, g, b], a) => `rgba(${r}, ${g}, ${b}, ${a})`;

// trailGradientLayer.colors / .locations: tail (0) to head (1).
const GRADIENT_STOPS = [
  [0, rgba(PALETTE.jade, 0.02)],
  [0.36, rgba(PALETTE.jade, 0.58)],
  [0.76, rgba(PALETTE.ivory, 0.86)],
  [1.0, rgba(PALETTE.lagoon, 0.54)],
];

// -- pure geometry, no canvas/DOM state --------------------------------------

/** Catmull-Rom-style 0.25 / 0.5 / 0.25 pass; endpoints are left untouched. */
function smoothTrail(samples) {
  if (samples.length <= 2) return samples;
  return samples.map((c, i, arr) => {
    if (i === 0 || i === arr.length - 1) return c;
    const p = arr[i - 1];
    const n = arr[i + 1];
    return {
      x: p.x * 0.25 + c.x * 0.5 + n.x * 0.25,
      y: p.y * 0.25 + c.y * 0.5 + n.y * 0.25,
      t: c.t, // position is smoothed, age is not
    };
  });
}

/**
 * Left/right ribbon-edge points for points[index], and its half-width. The tangent is the
 * chord from the previous point to the next (clamped at the ends); rotating it 90 degrees
 * gives the outward normal the edges walk out along. Width decays with age, so the ribbon
 * tapers to nothing at the tail and is fullest at the newest (head) sample.
 */
function ribbonEdge(points, index, t) {
  const prev = points[Math.max(index - 1, 0)];
  const next = points[Math.min(index + 1, points.length - 1)];
  const length = Math.max(Math.hypot(next.x - prev.x, next.y - prev.y), 0.001);
  const nx = -(next.y - prev.y) / length;
  const ny = (next.x - prev.x) / length;
  const age = Math.min(TRAIL_LIFETIME, Math.max(0, t - points[index].t));
  const width = MAX_HALF_WIDTH * (1 - age / TRAIL_LIFETIME) ** WIDTH_DECAY_EXPONENT;
  const point = points[index];
  return {
    left: { x: point.x + nx * width, y: point.y + ny * width },
    right: { x: point.x - nx * width, y: point.y - ny * width },
    width,
  };
}

/**
 * Quadratic-curve-through-midpoints smoothing: each interior point curves toward the
 * midpoint of itself and its neighbor, using itself as the control point; the pen is
 * assumed to already sit on points[0]. The final point is a plain lineTo -- a quadratic
 * curve whose control point equals its destination is exactly a line, not an approximation.
 */
function addSmoothCurve(path, points) {
  if (points.length < 2) return;
  if (points.length === 2) {
    path.lineTo(points[1].x, points[1].y);
    return;
  }
  for (let i = 1; i < points.length; i += 1) {
    const point = points[i];
    if (i === points.length - 1) {
      path.lineTo(point.x, point.y);
      continue;
    }
    const next = points[i + 1];
    path.quadraticCurveTo(point.x, point.y, (point.x + next.x) / 2, (point.y + next.y) / 2);
  }
}

/** Closed ribbon outline: left edge tail->head, a rounded head cap, right edge head->tail. */
function buildRibbonPath(smoothed, t) {
  const edges = smoothed.map((_, i) => ribbonEdge(smoothed, i, t));
  const left = edges.map((e) => e.left);
  const right = edges.map((e) => e.right);
  const path = new Path2D();
  path.moveTo(left[0].x, left[0].y);
  addSmoothCurve(path, left);

  const head = smoothed[smoothed.length - 1];
  const headEdge = edges[edges.length - 1];
  if (headEdge.width > ARC_MIN_WIDTH) {
    const startAngle = Math.atan2(headEdge.left.y - head.y, headEdge.left.x - head.x);
    const endAngle = Math.atan2(headEdge.right.y - head.y, headEdge.right.x - head.x);
    // Verified empirically against CGPath's addArc (which UIBezierPath sits on top of):
    // in this Y-down context, Swift's `clockwise: true` sweeps through *decreasing* angle
    // here -- canvas's `counterclockwise: true` -- bulging the cap toward the direction of
    // travel rather than back over the ribbon body.
    path.arc(head.x, head.y, headEdge.width, startAngle, endAngle, true);
  }
  addSmoothCurve(path, [right[right.length - 1], ...right.slice(0, -1).reverse()]);
  path.closePath();
  return path;
}

// -- renderer -----------------------------------------------------------------

export function createGlideTrail(canvas) {
  const ctx = canvas.getContext("2d");
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");

  let samples = []; // {x, y, t}: CSS px and seconds, oldest first
  let lastPoint = null;
  let active = false;
  let evaporationStart = null;
  let rafId = null;
  let cssWidth = 0;
  let cssHeight = 0;

  const now = () => performance.now() / 1000;
  const pruneSamples = (t) => {
    samples = samples.filter((s) => t - s.t <= TRAIL_LIFETIME);
  };

  function drawRibbon(smoothed, t) {
    const path = buildRibbonPath(smoothed, t);
    ctx.save();
    ctx.shadowColor = rgba(PALETTE.jade, 0.64);
    ctx.shadowBlur = 8;
    ctx.fillStyle = rgba(PALETTE.jade, 0.28);
    ctx.fill(path); // glow pass, sits under the ribbon (lower zPosition in Swift)
    ctx.restore();

    // Gradient runs tail -> head so the color sweep reads as motion toward the fingertip,
    // matching trailGradientLayer's startPoint (tail) / endPoint (head) in the Swift source.
    const tail = smoothed[0];
    const head = smoothed[smoothed.length - 1];
    const gradient = ctx.createLinearGradient(tail.x, tail.y, head.x, head.y);
    for (const [offset, color] of GRADIENT_STOPS) gradient.addColorStop(offset, color);
    ctx.fillStyle = gradient;
    ctx.fill(path);
    ctx.strokeStyle = rgba(PALETTE.ivory, 0.4);
    ctx.lineWidth = 1;
    ctx.stroke(path);
  }

  function draw(t) {
    ctx.clearRect(0, 0, cssWidth, cssHeight);
    if (samples.length < 2) return;
    if (reduceMotion.matches) {
      // Reduced motion: the current path only, no width/age animation, no glow.
      ctx.beginPath();
      ctx.moveTo(samples[0].x, samples[0].y);
      for (let i = 1; i < samples.length; i += 1) ctx.lineTo(samples[i].x, samples[i].y);
      ctx.lineCap = "round";
      ctx.lineJoin = "round";
      ctx.strokeStyle = rgba(PALETTE.ivory, 0.7);
      ctx.lineWidth = 2;
      ctx.stroke();
      return;
    }
    drawRibbon(smoothTrail(samples), t);
  }

  const stopLoop = () => {
    if (rafId !== null) {
      cancelAnimationFrame(rafId);
      rafId = null;
    }
  };

  function tick() {
    rafId = null;
    const t = now();
    if (active && lastPoint) {
      // Re-stamp the head every frame while down, so it stays full-width mid-pause instead
      // of aging under its last sample -- matches displayLinkDidTick's refresh of the tail.
      const head = { x: lastPoint.x, y: lastPoint.y, t };
      if (samples.length === 0) samples.push(head);
      else samples[samples.length - 1] = head;
    }
    pruneSamples(t);
    draw(t);
    if (!active && evaporationStart !== null && t - evaporationStart >= EVAPORATION_DURATION) {
      clear();
      return;
    }
    if (active || evaporationStart !== null) rafId = requestAnimationFrame(tick);
  }

  function ensureAnimating() {
    if (reduceMotion.matches) {
      draw(now()); // event-driven only -- no continuous loop under reduced motion
      return;
    }
    if (rafId === null) rafId = requestAnimationFrame(tick);
  }

  function resize() {
    const rect = canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    cssWidth = rect.width;
    cssHeight = rect.height;
    canvas.width = Math.max(1, Math.round(cssWidth * dpr));
    canvas.height = Math.max(1, Math.round(cssHeight * dpr));
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0); // draw calls above stay in CSS px
    draw(now());
  }

  function push(x, y) {
    const t = now();
    if (!active) {
      // Fresh touch-down: drop anything still evaporating from the last gesture so it
      // never blends into the new glide.
      samples = [];
      evaporationStart = null;
      active = true;
    }
    samples.push({ x, y, t });
    lastPoint = { x, y };
    pruneSamples(t);
    ensureAnimating();
  }

  function lift() {
    if (!active) return;
    active = false;
    if (reduceMotion.matches) {
      clear(); // nothing animates under reduced motion, so nothing to wait out
      return;
    }
    evaporationStart = now();
    ensureAnimating();
  }

  function clear() {
    active = false;
    evaporationStart = null;
    samples = [];
    lastPoint = null;
    stopLoop();
    ctx.clearRect(0, 0, cssWidth, cssHeight);
  }

  function destroy() {
    clear();
    resizeObserver.disconnect();
    reduceMotion.removeEventListener("change", onMotionChange);
  }

  const onMotionChange = () => draw(now());
  reduceMotion.addEventListener("change", onMotionChange);
  const resizeObserver = new ResizeObserver(resize);
  resizeObserver.observe(canvas);
  resize();

  return { push, lift, clear, destroy };
}
