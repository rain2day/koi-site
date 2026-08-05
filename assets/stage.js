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

/* ---- the pond ------------------------------------------------------------ */

const pondCanvas = document.querySelector("[data-koi-pond]");

function pondWanted() {
  if (!pondCanvas) return false;
  if (reduceMotion.matches) return false;
  const probe = document.createElement("canvas");
  return Boolean(probe.getContext("webgl2") || probe.getContext("webgl"));
}

wireInk();

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
