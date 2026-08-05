/* Connects the pond to the keyboard.
 *
 * Kept separate from both so each stays useful alone: the demo works with no
 * pond behind it, and the pond runs whether or not anything is dropping into
 * it. This module is only the wire between them.
 *
 * It is also the gate on the graphics library. The pond is the one part of the
 * site with a real dependency, and it is the part a visitor is least likely to
 * need — so the import is dynamic and happens only once the scene is known to
 * be both wanted and possible. A phone that asked for reduced motion, or a
 * browser without WebGL, never downloads it.
 */

const canvas = document.querySelector("[data-koi-pond]");

function wanted() {
  if (!canvas) return false;
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return false;
  const probe = document.createElement("canvas");
  return Boolean(probe.getContext("webgl2") || probe.getContext("webgl"));
}

if (wanted()) {
  import("./pond.js").then(({ createPond }) => {
    const pond = createPond(canvas);
    if (!pond) return;

    // Characters land where the keyboard actually is, so the ripple reads as
    // having come from the thing you just did rather than from nowhere.
    const originOf = (element) => {
      if (!element) return { x: 0.5, y: 0.62 };
      const pondBox = canvas.getBoundingClientRect();
      const box = element.getBoundingClientRect();
      const x = (box.left + box.width / 2 - pondBox.left) / pondBox.width;
      const y = 1 - (box.top - pondBox.top) / pondBox.height;
      return {
        x: Math.min(Math.max(x, 0.06), 0.94),
        y: Math.min(Math.max(y, 0.06), 0.94),
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
  });
}
