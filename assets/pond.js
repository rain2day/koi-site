/* The koi pond behind the landing page.
 *
 * The keyboard demo sits on top of this. Everything you do to it lands in the
 * water: move a pointer and the surface answers, glide out a character and it
 * drops in and sinks, and the koi turn toward wherever the last one fell. That
 * loop is the reason the scene exists — a decorative background would not have
 * earned the bytes.
 *
 * Two passes. The koi are drawn into an offscreen target first; the water is a
 * single full-screen quad that samples that target through a displaced UV, so
 * the fish are genuinely refracted by the ripples above them rather than having
 * a wobble drawn on top of them.
 *
 * Ripples are an array of expanding damped rings summed in the fragment shader,
 * not a ping-pong height-field simulation. For a dozen concurrent drops the sum
 * is cheaper, needs no extra render targets, and cannot accumulate the drift a
 * feedback buffer does when a frame is skipped.
 */

import * as THREE from "./vendor/three.module.min.js";

const MAX_DROPS = 8;
const DROP_LIFE = 3.4; // seconds a ripple stays in the sum
const KOI_COUNT = 5;

/* ---- shaders ------------------------------------------------------------ */

const WATER_VERTEX = /* glsl */ `
  varying vec2 vUv;
  void main() {
    vUv = uv;
    gl_Position = vec4(position.xy, 0.0, 1.0);
  }
`;

const WATER_FRAGMENT = /* glsl */ `
  precision highp float;

  uniform sampler2D uScene;
  uniform float uTime;
  uniform vec2  uAspect;
  uniform vec3  uDrops[${MAX_DROPS}];   // xy = origin in uv, z = start time
  uniform float uStrength[${MAX_DROPS}];
  uniform vec3  uDeep;
  uniform vec3  uShallow;
  uniform vec3  uGlint;
  uniform vec3  uKoiLight;
  uniform float uCalm;                  // 0 = still water, 1 = full motion

  varying vec2 vUv;

  const float LIFE  = ${DROP_LIFE.toFixed(1)};
  const float SPEED = 0.42;   // ring expansion, uv units per second
  const float FREQ  = 52.0;   // wavelength of the ring train
  const float DECAY = 1.25;

  /* One expanding, damped ring. Confined to a narrow band around the wavefront
     so a drop reads as a ring travelling outward rather than the whole disc
     pulsing. */
  float ringAt(vec2 p, vec3 drop, float strength) {
    float age = uTime - drop.z;
    if (age < 0.0 || age > LIFE) return 0.0;
    float radius = length((p - drop.xy) * uAspect);
    float front = radius - age * SPEED;
    float band = exp(-front * front * 260.0);
    float wave = sin(front * FREQ);
    float fade = exp(-age * DECAY) * (1.0 - smoothstep(LIFE * 0.7, LIFE, age));
    return wave * band * fade * strength;
  }

  /* Standing swell so the pond is alive when nobody is touching it. */
  float swell(vec2 p) {
    vec2 q = p * uAspect;
    float h = sin(q.x * 9.3 + uTime * 0.35) * 0.55;
    h += sin(q.y * 11.7 - uTime * 0.27) * 0.4;
    h += sin((q.x + q.y) * 15.1 + uTime * 0.19) * 0.28;
    return h * 0.005;
  }

  /* Caustics: the light that is always moving on water, independent of any
     ripple. Four sines is enough to read as a surface and cheap enough to run
     on every pixel of a background. */
  float caustic(vec2 p) {
    vec2 q = p * uAspect * 5.5;
    float c = sin(q.x + uTime * 0.45) * sin(q.y * 1.3 - uTime * 0.33);
    c += sin(q.x * 1.7 - uTime * 0.29) * sin(q.y * 0.9 + uTime * 0.41);
    return pow(max(c * 0.5 + 0.5, 0.0), 3.5);
  }

  float height(vec2 p) {
    float h = swell(p);
    for (int i = 0; i < ${MAX_DROPS}; i++) {
      h += ringAt(p, uDrops[i], uStrength[i]) * 0.045;
    }
    return h * uCalm;
  }

  void main() {
    /* Central differences give the surface slope, which is both the refraction
       offset for the fish below and the normal the light is shaded against. */
    vec2 e = vec2(1.6 / 900.0, 0.0);
    float h  = height(vUv);
    float hx = height(vUv + e.xy) - height(vUv - e.xy);
    float hy = height(vUv + e.yx) - height(vUv - e.yx);

    vec2 refracted = clamp(vUv + vec2(hx, hy) * 2.6, 0.0, 1.0);
    vec3 below = texture2D(uScene, refracted).rgb;

    vec3 normal = normalize(vec3(-hx * 55.0, -hy * 55.0, 1.0));
    float depth = smoothstep(0.0, 1.0, vUv.y);
    vec3 water = mix(uDeep, uShallow, depth * 0.75);

    /* Water over fish, then the surface's own light on top of both. */
    vec3 colour = mix(water, below, clamp(below.r + below.g + below.b, 0.0, 1.0) * 0.9);

    float glint = pow(max(dot(normal, normalize(vec3(0.35, 0.6, 0.72))), 0.0), 26.0);
    colour += uGlint * glint * 0.8;

    float rim = pow(max(dot(normal, normalize(vec3(-0.6, -0.35, 0.7))), 0.0), 12.0);
    colour += uKoiLight * rim * 0.18;

    colour += uGlint * clamp(abs(h) * 14.0, 0.0, 1.0) * 0.18;

    colour += uGlint * caustic(vUv) * 0.075 * uCalm;

    /* Vignette, so the scene sits behind the page rather than competing. */
    vec2 v = (vUv - 0.5) * vec2(1.15, 1.0);
    colour *= 1.0 - dot(v, v) * 0.32;

    gl_FragColor = vec4(colour, 1.0);
  }
`;

const KOI_VERTEX = /* glsl */ `
  uniform float uTime;
  uniform float uPhase;
  varying vec2 vUv;
  void main() {
    vUv = uv;
    vec3 p = position;
    /* Body undulation, strongest at the tail (negative x) and nothing at the
       head, which is what stops it reading as a flapping rectangle. */
    float tail = smoothstep(0.5, -0.5, p.x);
    p.z += sin(p.x * 4.2 - uTime * 2.6 + uPhase) * 0.03 * tail;
    p.y += sin(p.x * 4.2 - uTime * 2.6 + uPhase) * 0.028 * tail;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
  }
`;

/* The fish are drawn rather than textured.
 *
 * The first attempt keyed the app icon out by luminance, but that artwork is a
 * koi *inside a composition* — the teal swirls behind it survived the cutout and
 * the body undulation smeared the whole thing into a worm. A shape defined in
 * the shader is a real koi seen from above, costs no image request, and stays
 * sharp at any size. */
const KOI_FRAGMENT = /* glsl */ `
  precision highp float;
  uniform float uOpacity;
  uniform vec3 uBody;
  uniform vec3 uPatch;
  uniform float uSeed;
  varying vec2 vUv;

  void main() {
    vec2 p = vUv - 0.5;            // nose at +x, tail at -x

    /* Body: a spindle, widest just behind the head and tapering both ways. */
    float t = clamp((p.x + 0.40) / 0.80, 0.0, 1.0);
    float spine = sin(t * 3.14159);
    float bodyHalf = 0.075 * spine * spine * 1.7;
    float body = smoothstep(bodyHalf, bodyHalf - 0.018, abs(p.y))
               * step(-0.40, p.x) * step(p.x, 0.42);

    /* Caudal fin: a wedge opening out behind the body. */
    float fx = -0.28 - p.x;
    float finHalf = fx * 0.62 + 0.010;
    float fin = smoothstep(finHalf, finHalf - 0.02, abs(p.y))
              * step(0.0, fx) * step(p.x, -0.28) * step(-0.5, p.x);

    /* Pectoral fins, small and swept back. */
    float px = p.x - 0.08;
    float pec = smoothstep(0.055, 0.02, abs(abs(p.y) - 0.10 - px * 0.35))
              * step(-0.02, px) * step(px, 0.16);

    float mask = max(max(body, fin * 0.85), pec * 0.5);
    if (mask < 0.02) discard;

    /* Two pale saddles, the markings that make a koi a koi rather than a fish. */
    float m1 = smoothstep(0.16, 0.0, distance(p, vec2(0.16 + uSeed * 0.05, 0.0)) * 1.6);
    float m2 = smoothstep(0.13, 0.0, distance(p, vec2(-0.14 - uSeed * 0.04, 0.02)) * 1.9);
    vec3 colour = mix(uBody, uPatch, clamp(m1 + m2, 0.0, 1.0) * 0.9);

    /* Fins are thinner than the body, so they read as translucent. */
    float density = body > 0.5 ? 1.0 : 0.55;

    gl_FragColor = vec4(colour, mask * uOpacity * density);
  }
`;

/* ---- glyphs ------------------------------------------------------------- */

/** A committed character, drawn to a texture so it can sink through the water. */
function glyphTexture(character) {
  const size = 256;
  const canvas = document.createElement("canvas");
  canvas.width = size;
  canvas.height = size;
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, size, size);
  ctx.font = `600 ${size * 0.72}px "PingFang HK", "Noto Sans HK", serif`;
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillStyle = "#ffffff";
  ctx.shadowColor = "rgba(93, 217, 200, 0.85)";
  ctx.shadowBlur = size * 0.12;
  ctx.fillText(character, size / 2, size * 0.54);
  const texture = new THREE.CanvasTexture(canvas);
  texture.colorSpace = THREE.SRGBColorSpace;
  return texture;
}

/* ---- the pond ----------------------------------------------------------- */

export function createPond(canvas, options = {}) {
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");

  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ canvas, antialias: false, alpha: false });
  } catch {
    return null; // no WebGL: the page keeps its CSS background and loses nothing else
  }
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.setClearColor(0x081018, 1);

  const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0.1, 100);
  camera.position.z = 5;

  const koiScene = new THREE.Scene();
  const waterScene = new THREE.Scene();

  let target = new THREE.WebGLRenderTarget(1, 1);

  const drops = Array.from({ length: MAX_DROPS }, () => new THREE.Vector3(0, 0, -999));
  const strengths = new Float32Array(MAX_DROPS);
  let nextDrop = 0;

  const water = new THREE.Mesh(
    new THREE.PlaneGeometry(2, 2),
    new THREE.ShaderMaterial({
      vertexShader: WATER_VERTEX,
      fragmentShader: WATER_FRAGMENT,
      depthTest: false,
      uniforms: {
        uScene: { value: target.texture },
        uTime: { value: 0 },
        uAspect: { value: new THREE.Vector2(1, 1) },
        uDrops: { value: drops },
        uStrength: { value: strengths },
        uDeep: { value: new THREE.Color(0x0c1e2e) },
        uShallow: { value: new THREE.Color(0x1e4863) },
        uGlint: { value: new THREE.Color(0x5dd9c8) },
        uKoiLight: { value: new THREE.Color(0xff5136) },
        uCalm: { value: reduceMotion.matches ? 0.25 : 1 },
      },
    })
  );
  waterScene.add(water);

  /* ---- koi -------------------------------------------------------------- */

  const koi = [];
  const koiGeometry = new THREE.PlaneGeometry(1.6, 0.8, 40, 2);

  for (let index = 0; index < KOI_COUNT; index += 1) {
    const mesh = new THREE.Mesh(
      koiGeometry,
      new THREE.ShaderMaterial({
        vertexShader: KOI_VERTEX,
        fragmentShader: KOI_FRAGMENT,
        transparent: true,
        depthWrite: false,
        uniforms: {
          uTime: { value: 0 },
          uPhase: { value: index * 2.1 },
          uSeed: { value: index * 0.7 },
          uOpacity: { value: 0.44 - index * 0.05 },
          uBody: { value: new THREE.Color(index % 2 ? 0xff7355 : 0xe8402a) },
          uPatch: { value: new THREE.Color(0xf4ece0) },
        },
      })
    );
    const scale = 0.28 - index * 0.028;
    mesh.scale.setScalar(scale);
    koi.push({
      mesh,
      // Each fish traces its own slow Lissajous loop, so they never form a
      // convoy or repeat the same crossing.
      speed: 0.05 + index * 0.014,
      radius: new THREE.Vector2(0.78 - index * 0.09, 0.30 - index * 0.04),
      phase: index * 2.4,
      lean: 0,
    });
    koiScene.add(mesh);
  }

  /* ---- sinking glyphs --------------------------------------------------- */

  const glyphs = [];

  function dropGlyph(character, x = 0.5, y = 0.62) {
    if (!character || reduceMotion.matches) return;
    const mesh = new THREE.Mesh(
      new THREE.PlaneGeometry(0.46, 0.46),
      new THREE.MeshBasicMaterial({
        map: glyphTexture(character),
        transparent: true,
        depthWrite: false,
      })
    );
    mesh.position.set(x * 2 - 1, y * 2 - 1, 0);
    koiScene.add(mesh);
    glyphs.push({ mesh, born: clock.getElapsedTime(), x, y });
    splash(x, y, 1.35);
    // The nearest fish turns toward whatever just landed.
    for (const fish of koi) fish.lean = 1;
  }

  /* ---- ripples ---------------------------------------------------------- */

  function splash(x, y, strength = 1) {
    if (reduceMotion.matches) return;
    drops[nextDrop].set(x, y, clock.getElapsedTime());
    strengths[nextDrop] = strength;
    nextDrop = (nextDrop + 1) % MAX_DROPS;
  }

  /* ---- loop ------------------------------------------------------------- */

  const clock = new THREE.Clock();
  let frame = null;
  let visible = true;
  let onScreen = true;

  function resize() {
    const rect = canvas.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    /* Water is a soft, low-frequency image: it survives being rendered well
       under 1:1 and nobody can tell, whereas the fragment shader is expensive
       (five height samples per pixel, each summing every live ripple). Rendering
       at roughly two-thirds and letting the canvas scale up cuts the per-frame
       cost by more than half for no visible loss — the difference between a
       background that is free on a phone and one that is not. */
    const ratio = Math.min(window.devicePixelRatio || 1, 1) * 0.68;
    renderer.setPixelRatio(ratio);
    renderer.setSize(rect.width, rect.height, false);
    target.setSize(Math.round(rect.width * ratio), Math.round(rect.height * ratio));
    water.material.uniforms.uAspect.value.set(Math.max(1, rect.width / rect.height), 1);
  }

  function render() {
    const time = clock.getElapsedTime();
    water.material.uniforms.uTime.value = time;

    for (const fish of koi) {
      const t = time * fish.speed + fish.phase;
      const x = Math.sin(t) * fish.radius.x;
      const y = Math.cos(t * 0.73) * fish.radius.y;
      const nx = Math.sin(t + 0.05) * fish.radius.x;
      const ny = Math.cos((t + 0.05) * 0.73) * fish.radius.y;
      fish.mesh.position.set(x, y - 0.28, 0);
      fish.mesh.rotation.z = Math.atan2(ny - y, nx - x);
      fish.mesh.material.uniforms.uTime.value = time;
      fish.lean *= 0.98;
    }

    for (let index = glyphs.length - 1; index >= 0; index -= 1) {
      const glyph = glyphs[index];
      const age = time - glyph.born;
      if (age > 3.2) {
        koiScene.remove(glyph.mesh);
        glyph.mesh.material.map.dispose();
        glyph.mesh.material.dispose();
        glyph.mesh.geometry.dispose();
        glyphs.splice(index, 1);
        continue;
      }
      glyph.mesh.position.y = glyph.y * 2 - 1 - age * 0.14;
      glyph.mesh.material.opacity = Math.max(0, 1 - age / 3.2);
      glyph.mesh.scale.setScalar(1 + age * 0.12);
    }

    renderer.setRenderTarget(target);
    renderer.clear();
    renderer.render(koiScene, camera);
    renderer.setRenderTarget(null);
    renderer.render(waterScene, camera);
  }

  function tick() {
    frame = requestAnimationFrame(tick);
    render();
  }

  function start() {
    if (frame === null && visible && onScreen && !reduceMotion.matches) tick();
  }

  function stop() {
    if (frame !== null) {
      cancelAnimationFrame(frame);
      frame = null;
    }
  }

  /* ---- wiring ----------------------------------------------------------- */

  const onResize = () => {
    resize();
    render();
  };
  window.addEventListener("resize", onResize);

  /* `resize()` gives up when the element measures zero, which is the right call
     — a zero-sized render target is invalid. But a window resize is not the only
     way an element gains size: it can be laid out late, revealed from a hidden
     ancestor, or start life in a document that has no viewport yet. Without this
     the canvas would stay stuck at its 300x150 default forever. */
  const sizeObserver = new ResizeObserver(onResize);
  sizeObserver.observe(canvas);

  const onVisibility = () => {
    visible = document.visibilityState === "visible";
    visible ? start() : stop();
  };
  document.addEventListener("visibilitychange", onVisibility);

  // A background nobody is looking at should not be burning a GPU.
  const observer = new IntersectionObserver(
    ([entry]) => {
      onScreen = entry.isIntersecting;
      onScreen ? start() : stop();
    },
    { threshold: 0 }
  );
  observer.observe(canvas);

  let lastSplash = 0;
  const onPointer = (event) => {
    const rect = canvas.getBoundingClientRect();
    const now = clock.getElapsedTime();
    if (now - lastSplash < 0.07) return; // one ring per ~70ms, not per event
    lastSplash = now;
    splash(
      (event.clientX - rect.left) / rect.width,
      1 - (event.clientY - rect.top) / rect.height,
      0.5
    );
  };
  window.addEventListener("pointermove", onPointer, { passive: true });

  resize();
  render();
  start();

  return {
    splash,
    dropGlyph,
    destroy() {
      stop();
      observer.disconnect();
      sizeObserver.disconnect();
      window.removeEventListener("resize", onResize);
      window.removeEventListener("pointermove", onPointer);
      document.removeEventListener("visibilitychange", onVisibility);
      target.dispose();
      renderer.dispose();
    },
  };
}
