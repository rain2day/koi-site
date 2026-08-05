/* Wires the landing page's interactive parts to each other.
 *
 * Kept separate from all of them so each stays useful alone: the keyboard works
 * with no pond behind it, the pond runs whether or not anything drops into it,
 * and the write-on-water panel needs neither. This module is only the wiring.
 *
 * It is also the gate on the graphics library. The pond is the one part of the
 * site with a real dependency, and the part a visitor is least likely to need,
 * so its import is dynamic and happens only once a scene is known to be both
 * wanted and possible. Everything else here is plain canvas and always runs.
 */

import { createGlideTrail } from "./glide-trail.js";

const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");

/* ---- write on water ------------------------------------------------------
 * KOI draws its handwriting area as a water surface. This is the honest web
 * equivalent: the ink is the keyboard's own glide trail, on a surface styled
 * like the pond. Recognition is not here — that model runs on the device — and
 * the copy beside it says so.
 *
 * It needs nothing else on the page, so it is wired unconditionally: plain
 * canvas, no WebGL, no dependency.
 */

function wireInk() {
  const canvas = document.querySelector("[data-koi-ink]");
  if (!canvas) return;

  const trail = createGlideTrail(canvas);
  let drawing = false;

  const at = (event) => {
    const box = canvas.getBoundingClientRect();
    return { x: event.clientX - box.left, y: event.clientY - box.top, box };
  };

  canvas.addEventListener("pointerdown", (event) => {
    if (event.pointerType === "mouse" && event.button !== 0) return;
    drawing = true;
    const { x, y } = at(event);
    trail.push(x, y);
    try {
      canvas.setPointerCapture(event.pointerId);
    } catch {
      /* not capturable — the stroke still works */
    }
  });

  canvas.addEventListener("pointermove", (event) => {
    if (!drawing) return;
    const { x, y } = at(event);
    trail.push(x, y);
  });

  const stop = () => {
    if (!drawing) return;
    drawing = false;
    trail.lift();
  };
  canvas.addEventListener("pointerup", stop);
  canvas.addEventListener("pointercancel", stop);
  canvas.addEventListener("pointerleave", stop);
}

/* ---- the film ------------------------------------------------------------
 * The markup ships paused, with a poster and native controls, so a visitor with
 * no JavaScript gets a still and a play button rather than a dead rectangle,
 * and a visitor who asked for reduced motion is never handed a loop. Autoplay
 * is granted here, and only here.
 */

function wireFilm() {
  const film = document.querySelector("[data-koi-film]");
  if (!film || reduceMotion.matches) return;

  film.controls = false;

  // Nothing is fetched until the film is nearly on screen, and it stops again
  // when it leaves — a five-second loop running behind six screens of text is
  // just a battery cost.
  const watcher = new IntersectionObserver(
    ([entry]) => {
      if (!entry.isIntersecting) {
        film.pause();
        return;
      }
      film.preload = "auto";
      film.play().catch(() => {
        // Autoplay refused. Hand the visitor the controls back rather than
        // leaving them looking at a poster that never moves.
        film.controls = true;
      });
    },
    { rootMargin: "250px" }
  );
  watcher.observe(film);
}

/* ---- the hint ------------------------------------------------------------
 * The first time the keyboard comes into view it draws one ghost stroke through
 * h, d and a — the same ink the demo uses, on the same canvas, but nothing is
 * decoded and nothing is committed. It answers "what am I supposed to do here?"
 * without doing it for you.
 */

function wireHint() {
  const keys = document.querySelector(".kbd-keys");
  const canvas = keys && keys.querySelector(".kbd-trail");
  if (!keys || !canvas || reduceMotion.matches) return;

  const trail = createGlideTrail(canvas);
  let played = false;

  const centreOf = (letter) => {
    const key = keys.querySelector(`[data-letter="${letter}"]`);
    if (!key) return null;
    const box = keys.getBoundingClientRect();
    const rect = key.getBoundingClientRect();
    return { x: rect.left + rect.width / 2 - box.left, y: rect.top + rect.height / 2 - box.top };
  };

  const draw = () => {
    const path = ["h", "d", "a"].map(centreOf);
    if (path.some((point) => point === null)) return;
    const start = performance.now();
    const DURATION = 1150;

    const step = (now) => {
      const progress = Math.min(1, (now - start) / DURATION);
      // Ease out, so the ghost decelerates into a the way a finger does.
      const eased = 1 - Math.pow(1 - progress, 3);
      const span = eased * (path.length - 1);
      const leg = Math.min(path.length - 2, Math.floor(span));
      const t = span - leg;
      trail.push(
        path[leg].x + (path[leg + 1].x - path[leg].x) * t,
        path[leg].y + (path[leg + 1].y - path[leg].y) * t
      );
      if (progress < 1) requestAnimationFrame(step);
      else trail.lift();
    };
    requestAnimationFrame(step);
  };

  const watcher = new IntersectionObserver(
    ([entry]) => {
      if (!entry.isIntersecting || played) return;
      played = true;
      watcher.disconnect();
      setTimeout(draw, 450);
    },
    { threshold: 0.55 }
  );
  watcher.observe(keys);
}

/* ---- the pond ------------------------------------------------------------ */

const pondCanvas = document.querySelector("[data-koi-pond]");

function pondWanted() {
  if (!pondCanvas) return false;
  if (reduceMotion.matches) return false;
  const probe = document.createElement("canvas");
  return Boolean(probe.getContext("webgl2") || probe.getContext("webgl"));
}

wireInk();
wireFilm();
wireHint();

if (pondWanted()) {
  import("./pond.js")
    .then(({ createPond }) => {
      const pond = createPond(pondCanvas);
      if (!pond) return;

      // Characters land where the keyboard actually is, so the ripple reads as
      // having come from the thing you just did rather than from nowhere.
      const originOf = (element) => {
        if (!element) return { x: 0.5, y: 0.62 };
        const pondBox = pondCanvas.getBoundingClientRect();
        const box = element.getBoundingClientRect();
        return {
          x: Math.min(Math.max((box.left + box.width / 2 - pondBox.left) / pondBox.width, 0.06), 0.94),
          y: Math.min(Math.max(1 - (box.top - pondBox.top) / pondBox.height, 0.06), 0.94),
        };
      };

      document.addEventListener("koi:commit", (event) => {
        const character = event.detail && event.detail.character;
        if (!character) return;
        const { x, y } = originOf(document.querySelector(".kbd-screen"));
        pond.dropGlyph(character, x, y);
      });

      // A stroke that decodes to nothing still disturbed the water.
      document.addEventListener("koi:stroke", () => {
        const { x, y } = originOf(document.querySelector(".kbd-keys"));
        pond.splash(x, y, 0.75);
      });
    })
    .catch(() => {
      /* No scene. The rest of the page is unaffected. */
    });
}
