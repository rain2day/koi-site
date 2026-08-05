/* A working Cangjie input method, running entirely in this page.
 *
 * This is the site's central claim made touchable: KOI's typing engine never
 * reaches the network, and neither does this. There is no fetch, no analytics,
 * no state that outlives the tab. The dictionary is a static module the browser
 * caches once; every keystroke after that is resolved locally.
 *
 * It is a reduced copy of the shipping engine, not a reimplementation of it.
 * The radical mapping, the candidate ordering, the number-row-becomes-candidate
 * -row behaviour, the five-code ceiling and — the point of the whole thing —
 * glide decoding all match the iOS keyboard. Two-finger chorded entry, learning,
 * Tap Rescue and the other four input modes are not here, and the demo says so
 * rather than pretending otherwise.
 */

import { RADICALS, TABLE } from "./cangjie-data.js";
import { createPathSampler, decodeGlide } from "./glide-decoder.js";
import { createGlideTrail } from "./glide-trail.js";

const MAX_CODE_LENGTH = 5; // Cangjie never spells a character in more than five.
const MAX_CANDIDATES = 9; // The bar shows what the 1-9 selection keys can reach.
const SELECTION_KEYS = "123456789";

/* ---- dictionary ---------------------------------------------------------
 * The table arrives as newline-separated "code characters" lines, already
 * sorted by code. Splitting it into two parallel arrays lets a prefix lookup
 * binary-search the code column instead of building an index of every prefix,
 * which would cost more memory than the dictionary itself.
 */

const CODES = [];
const CHARS = [];

for (const line of TABLE.split("\n")) {
  const space = line.indexOf(" ");
  if (space > 0) {
    CODES.push(line.slice(0, space));
    CHARS.push(line.slice(space + 1));
  }
}

const EXACT = new Set(CODES);

/** Does any dictionary entry start with this code? Prunes the glide search. */
function hasPrefix(code) {
  const index = lowerBound(code);
  return index < CODES.length && CODES[index].startsWith(code);
}

/** The characters spelled by exactly this code, or "" if it is only a prefix. */
function charactersFor(code) {
  const index = lowerBound(code);
  return index < CODES.length && CODES[index] === code ? CHARS[index] : "";
}

/** Index of the first code >= target. */
function lowerBound(target) {
  let low = 0;
  let high = CODES.length;
  while (low < high) {
    const mid = (low + high) >> 1;
    if (CODES[mid] < target) low = mid + 1;
    else high = mid;
  }
  return low;
}

/**
 * Candidates for a partial code.
 *
 * An exact match always leads — typing `hqi` must offer 我 before anything
 * merely starting with `hqi` — and the rest follow in dictionary order, which
 * is the app's weight order and already carries the Hong Kong Cantonese boost.
 * Shorter codes come first among the prefix matches, so the character you are
 * closest to finishing is the one nearest your thumb.
 */
function lookup(code) {
  if (!code) return [];
  const exact = [];
  const prefixed = [];
  for (let i = lowerBound(code); i < CODES.length && CODES[i].startsWith(code); i += 1) {
    (CODES[i] === code ? exact : prefixed).push(i);
  }
  prefixed.sort((a, b) => CODES[a].length - CODES[b].length || a - b);

  const seen = new Set();
  const out = [];
  for (const index of exact.concat(prefixed)) {
    for (const character of CHARS[index]) {
      if (!seen.has(character)) {
        seen.add(character);
        out.push(character);
        if (out.length === MAX_CANDIDATES) return out;
      }
    }
  }
  return out;
}

/* ---- layout -------------------------------------------------------------
 * Mirrors the shipping keyboard: three letter rows, z carrying the wildcard
 * marker rather than a radical, and a bottom row whose agent key is present but
 * inert here because the demo has no account and makes no requests.
 */

const ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];

const STRINGS = {
  "zh-Hant": {
    space: "空格",
    hint: "在鍵盤上滑行寫出整個編碼，或逐鍵點按；用電腦亦可直接按實體鍵盤",
    placeholder: "在此試打",
    cleared: "已清除",
    candidates: "候選字",
    wildcard: "萬用字元（此示範未啟用）",
    agent: "KOI Agent（此示範未啟用）",
    shift: "上檔（此示範未啟用）",
    numbers: "數字（此示範未啟用）",
    delete: "刪除",
    reset: "清除",
    committed: "已輸入",
    noMatch: "這一筆沒有對應的候選字",
  },
  en: {
    space: "space",
    hint: "Glide across the radicals in one stroke, or tap them one by one",
    placeholder: "Type here",
    cleared: "Cleared",
    candidates: "Candidates",
    wildcard: "Wildcard (not enabled in this demo)",
    agent: "KOI Agent (not enabled in this demo)",
    shift: "Shift (not enabled in this demo)",
    numbers: "Numbers (not enabled in this demo)",
    delete: "Delete",
    reset: "Clear",
    committed: "Entered",
    noMatch: "That stroke has no reading",
  },
};

function copyForDocument() {
  return document.documentElement.lang === "en" ? STRINGS.en : STRINGS["zh-Hant"];
}

/* ---- the demo ----------------------------------------------------------- */

class CangjieDemo {
  constructor(root) {
    this.root = root;
    this.copy = copyForDocument();
    this.committed = "";
    this.code = "";
    this.candidates = [];
    this.glideCandidates = null;
    this.suppressClick = false;
    this.build();
    this.render();
  }

  build() {
    const { copy } = this;

    this.output = document.createElement("div");
    this.output.className = "kbd-output";
    this.output.setAttribute("role", "textbox");
    this.output.setAttribute("aria-readonly", "true");
    this.output.setAttribute("aria-label", copy.placeholder);

    this.reset = document.createElement("button");
    this.reset.type = "button";
    this.reset.className = "kbd-reset";
    this.reset.textContent = copy.reset;
    this.reset.addEventListener("click", () => {
      this.committed = "";
      this.code = "";
      this.announce(copy.cleared);
      this.render();
      this.surface.focus();
    });

    const screen = document.createElement("div");
    screen.className = "kbd-screen";
    screen.append(this.output, this.reset);

    this.bar = document.createElement("div");
    this.bar.className = "kbd-bar";

    this.live = document.createElement("p");
    this.live.className = "kbd-live";
    this.live.setAttribute("aria-live", "polite");

    this.keys = document.createElement("div");
    this.keys.className = "kbd-keys";
    this.buildKeys();

    const hint = document.createElement("p");
    hint.className = "kbd-hint";
    hint.textContent = copy.hint;

    // One focusable surface for the whole demo: a visitor on a laptop clicks
    // once and then types normally. A per-key tabindex would make the keyboard
    // 30 stops of tab-through noise for someone who cannot use a pointer.
    this.surface = document.createElement("div");
    this.surface.className = "kbd-surface";
    this.surface.tabIndex = 0;
    this.surface.setAttribute("role", "application");
    this.surface.setAttribute("aria-label", copy.placeholder);
    this.surface.append(screen, this.bar, this.keys);
    this.surface.addEventListener("keydown", (event) => this.onKeyDown(event));

    this.root.append(this.surface, hint, this.live);
    this.setupGlide();
  }

  /* ---- glide -----------------------------------------------------------
   * The whole point of the keyboard: one stroke across the radicals instead of
   * a tap per radical. Pointer events go on the key container rather than the
   * keys, because a glide belongs to the path, not to whichever key happened to
   * be under the finger when it started. The per-key click handlers stay for
   * keyboard and assistive-technology users, suppressed for one event after a
   * stroke so a glide does not also register as a tap on the key it ended on.
   */

  setupGlide() {
    const canvas = document.createElement("canvas");
    canvas.className = "kbd-trail";
    canvas.setAttribute("aria-hidden", "true");
    this.keys.append(canvas);
    this.trail = createGlideTrail(canvas);

    let sampler = null;

    const localPoint = (event) => {
      const bounds = this.keys.getBoundingClientRect();
      return { x: event.clientX - bounds.left, y: event.clientY - bounds.top };
    };

    // Measured per stroke rather than cached: the keyboard is fluid, and a
    // resize or an orientation change between strokes would invalidate it.
    const keyFrames = () => {
      const bounds = this.keys.getBoundingClientRect();
      return [...this.keys.querySelectorAll("[data-letter]")].map((key) => {
        const rect = key.getBoundingClientRect();
        return {
          letter: key.dataset.letter,
          x: rect.left - bounds.left,
          y: rect.top - bounds.top,
          width: rect.width,
          height: rect.height,
        };
      });
    };

    this.keys.addEventListener("pointerdown", (event) => {
      if (event.pointerType === "mouse" && event.button !== 0) return;
      sampler = createPathSampler(keyFrames());
      const point = localPoint(event);
      sampler.begin(point);
      this.trail.push(point.x, point.y);
      // Capture keeps the stroke alive when the finger leaves the keyboard, but
      // it is not worth losing the stroke over: a pointer id the browser no
      // longer considers active throws, and the glide works fine without it.
      try {
        this.keys.setPointerCapture(event.pointerId);
      } catch {
        /* not capturable — carry on */
      }
      this.surface.focus();
    });

    this.keys.addEventListener("pointermove", (event) => {
      if (!sampler) return;
      const point = localPoint(event);
      sampler.move(point);
      if (sampler.isGliding) this.trail.push(point.x, point.y);
    });

    const finish = () => {
      if (!sampler) return;
      const segments = sampler.end();
      const glided = sampler.isGliding;
      sampler = null;
      this.trail.lift();
      if (glided && segments.length) {
        this.suppressClick = true;
        document.dispatchEvent(new CustomEvent("koi:stroke"));
        this.applyGlide(segments);
      }
    };

    this.keys.addEventListener("pointerup", finish);
    this.keys.addEventListener("pointercancel", finish);
  }

  applyGlide(segments) {
    const ranked = decodeGlide(segments, { isKnown: hasPrefix, isExact: (code) => EXACT.has(code) });

    if (!ranked.length) {
      // The device runs a best-first rescue search when the bounded one comes
      // back empty; the demo does not carry it, so the honest answer here is
      // that this stroke has no reading. Inventing one would be worse.
      this.code = "";
      this.glideCandidates = [];
      this.announce(this.copy.noMatch);
      this.render();
      return;
    }

    // Every code the stroke could have meant contributes candidates, in rank
    // order — the same thing the keyboard puts in front of you.
    const seen = new Set();
    const characters = [];
    for (const entry of ranked) {
      for (const character of charactersFor(entry.code)) {
        if (seen.has(character)) continue;
        seen.add(character);
        characters.push(character);
        if (characters.length === MAX_CANDIDATES) break;
      }
      if (characters.length === MAX_CANDIDATES) break;
    }

    this.code = ranked[0].code;
    this.glideCandidates = characters;
    this.render();
  }

  buildKeys() {
    const { copy } = this;

    for (const row of ROWS) {
      const line = document.createElement("div");
      line.className = "kbd-row";

      if (row === "zxcvbnm") {
        line.append(this.makeSpecial("⇧", "shift", copy.shift));
      }

      for (const letter of row) {
        line.append(this.makeLetter(letter));
      }

      if (row === "zxcvbnm") {
        const del = this.makeSpecial("⌫", "delete", copy.delete);
        del.addEventListener("click", () => this.backspace());
        line.append(del);
      }
      this.keys.append(line);
    }

    const bottom = document.createElement("div");
    bottom.className = "kbd-row kbd-row-bottom";
    bottom.append(this.makeSpecial("123", "numbers", copy.numbers));
    bottom.append(this.makeSpecial("✦", "agent", copy.agent));

    const space = this.makeSpecial(copy.space, "space", copy.space);
    space.addEventListener("click", () => this.commitFirst());
    bottom.append(space);

    const period = this.makeSpecial("。", "period", "。");
    period.addEventListener("click", () => this.insert("。"));
    bottom.append(period);
    this.keys.append(bottom);
  }

  makeLetter(letter) {
    const key = document.createElement("button");
    key.type = "button";
    key.className = "kbd-key";
    key.tabIndex = -1;
    key.dataset.letter = letter;

    const radical = document.createElement("span");
    radical.className = "kbd-radical";
    // z is the wildcard on the shipping keyboard, so it shows * where the
    // other keys show their radical.
    radical.textContent = letter === "z" ? "*" : RADICALS[letter] || "";

    const glyph = document.createElement("span");
    glyph.className = "kbd-glyph";
    glyph.textContent = letter;

    key.append(radical, glyph);
    key.setAttribute(
      "aria-label",
      letter === "z" ? `${letter} — ${this.copy.wildcard}` : `${letter} ${RADICALS[letter] || ""}`
    );
    key.addEventListener("click", () => this.press(letter));
    return key;
  }

  makeSpecial(label, name, ariaLabel) {
    const key = document.createElement("button");
    key.type = "button";
    key.className = `kbd-key kbd-key-${name}`;
    key.tabIndex = -1;
    key.textContent = label;
    key.setAttribute("aria-label", ariaLabel);
    if (name === "shift" || name === "numbers" || name === "agent") {
      key.disabled = true;
    }
    return key;
  }

  /* ---- input handling --------------------------------------------------- */

  press(letter) {
    if (this.suppressClick) {
      this.suppressClick = false;
      return;
    }
    this.glideCandidates = null;
    // z is inert: the shipping wildcard needs the full dictionary, and a key
    // that silently did nothing would read as a bug, so it is labelled instead.
    if (letter === "z") return;
    if (this.code.length >= MAX_CODE_LENGTH) return;
    this.code += letter;
    this.render();
  }

  backspace() {
    this.glideCandidates = null;
    if (this.code) this.code = this.code.slice(0, -1);
    else this.committed = [...this.committed].slice(0, -1).join("");
    this.render();
  }

  insert(character) {
    this.glideCandidates = null;
    // Announced rather than called directly: the pond listens if it is there,
    // and the demo neither knows nor cares whether anything is.
    document.dispatchEvent(
      new CustomEvent("koi:commit", { detail: { character } })
    );
    this.committed += character;
    this.code = "";
    this.render();
  }

  select(index) {
    const character = this.candidates[index];
    if (character) this.insert(character);
  }

  /** Space commits the leading candidate, matching the shipping keyboard. */
  commitFirst() {
    if (this.candidates.length) this.select(0);
    else if (this.code) this.code = "";
    else this.committed += " ";
    this.render();
  }

  onKeyDown(event) {
    if (event.metaKey || event.ctrlKey || event.altKey) return;
    const key = event.key;

    if (key === "Backspace") {
      event.preventDefault();
      this.backspace();
    } else if (key === " ") {
      event.preventDefault();
      this.commitFirst();
    } else if (key === "Escape") {
      event.preventDefault();
      this.code = "";
      this.render();
    } else if (this.code && SELECTION_KEYS.includes(key)) {
      event.preventDefault();
      this.select(Number(key) - 1);
    } else if (/^[a-zA-Z]$/.test(key)) {
      event.preventDefault();
      this.press(key.toLowerCase());
    }
  }

  announce(message) {
    this.live.textContent = message;
  }

  /* ---- rendering -------------------------------------------------------- */

  render() {
    this.candidates = this.glideCandidates || lookup(this.code);
    this.renderOutput();
    this.renderBar();
    this.reset.hidden = !this.committed && !this.code;
    for (const key of this.keys.querySelectorAll("[data-letter]")) {
      key.classList.toggle("is-live", this.code.endsWith(key.dataset.letter));
    }
  }

  renderOutput() {
    this.output.textContent = "";

    if (this.committed) {
      const done = document.createElement("span");
      done.className = "kbd-committed";
      done.textContent = this.committed;
      this.output.append(done);
    }

    if (this.code) {
      // The composing radicals are underlined the way marked text is on iOS:
      // provisional, still editable, not yet part of the document.
      const marked = document.createElement("span");
      marked.className = "kbd-marked";
      marked.textContent = [...this.code].map((letter) => RADICALS[letter] || letter).join("");
      this.output.append(marked);
    }

    if (!this.committed && !this.code) {
      const placeholder = document.createElement("span");
      placeholder.className = "kbd-placeholder";
      placeholder.textContent = this.copy.placeholder;
      this.output.append(placeholder);
    }

    const caret = document.createElement("span");
    caret.className = "kbd-caret";
    caret.setAttribute("aria-hidden", "true");
    this.output.append(caret);
  }

  renderBar() {
    this.bar.textContent = "";

    // Idle, the bar is the number row — exactly what the keyboard shows before
    // a composition starts. It becomes the candidate row on the first radical.
    if (!this.code) {
      this.bar.classList.remove("is-candidates");
      this.bar.removeAttribute("aria-label");
      for (const digit of "1234567890") {
        const cell = document.createElement("span");
        cell.className = "kbd-digit";
        cell.setAttribute("aria-hidden", "true");
        cell.textContent = digit;
        this.bar.append(cell);
      }
      return;
    }

    this.bar.classList.add("is-candidates");
    this.bar.setAttribute("aria-label", this.copy.candidates);

    this.candidates.forEach((character, index) => {
      const option = document.createElement("button");
      option.type = "button";
      option.className = "kbd-candidate";
      option.tabIndex = -1;

      const rank = document.createElement("span");
      rank.className = "kbd-rank";
      rank.setAttribute("aria-hidden", "true");
      rank.textContent = String(index + 1);

      const glyph = document.createElement("span");
      glyph.className = "kbd-candidate-glyph";
      glyph.textContent = character;

      option.append(rank, glyph);
      option.setAttribute("aria-label", `${index + 1} ${character}`);
      option.addEventListener("click", () => {
        this.select(index);
        this.surface.focus();
      });
      this.bar.append(option);
    });
  }
}

const root = document.querySelector("[data-cangjie-demo]");
if (root) {
  root.textContent = "";
  root.classList.add("is-ready");
  new CangjieDemo(root);
}
