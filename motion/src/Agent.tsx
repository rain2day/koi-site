/* KOI Agent — as a film.
 *
 * Two beats, both real flows: a message arrives and Reply drafts an answer for
 * one Credit; then Sticker draws one for six. The mode names and the Credit
 * costs are the shipping ones (catalog.js), and the counter on screen moves by
 * exactly those amounts.
 *
 * What this film does NOT do is impersonate the model. The drafted reply is
 * plainly a representative sentence, and the sticker is a drawn koi rather than
 * something dressed up as a generation that just came back from a server. The
 * flow is the claim; the output quality is not being demonstrated, and the
 * caption beside the film says so.
 *
 * Every value is a function of `useCurrentFrame()`. No CSS transitions: Remotion
 * renders frames out of order and anything on a wall clock would tear.
 */

import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { PALETTE } from "./keyboard";

export type Language = "zh" | "en";

const COPY = {
  zh: {
    incoming: "今晚七點旺角食飯？",
    modes: ["自動", "提問", "回覆", "改寫", "貼圖", "圖片"],
    reply: "好呀，我七點前到，見到再 WhatsApp 你。",
    drafting: "草擬回覆中",
    stickerPrompt: "一條錦鯉貼圖",
    credits: "Credits",
    replyCost: "回覆 −1",
    stickerCost: "貼圖 −6",
    transparent: "透明背景",
  },
  en: {
    incoming: "Dinner in Mong Kok at seven?",
    modes: ["Auto", "Ask", "Reply", "Rewrite", "Sticker", "Image"],
    reply: "Sounds good — I'll be there before seven, message me when you arrive.",
    drafting: "Drafting a reply",
    stickerPrompt: "a koi sticker",
    credits: "Credits",
    replyCost: "Reply −1",
    stickerCost: "Sticker −6",
    transparent: "Transparent background",
  },
} as const;

// Beats, in frames at 30fps.
const PANEL_IN = 22;
const REPLY_PICKED = 46;
const TYPE_FROM = 58;
const TYPE_TO = 116;
const INSERTED = 126;
const STICKER_PICKED = 156;
const STICKER_FROM = 168;
const STICKER_TO = 216;
const HOLD_UNTIL = 268;

const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const HAN = "'PingFang HK','Noto Sans HK',sans-serif";

/** A koi drawn for the film. Not a model output, and not presented as one. */
const KoiSticker: React.FC<{ scale: number; opacity: number }> = ({ scale, opacity }) => (
  <svg width={210} height={210} viewBox="-60 -60 120 120" style={{ transform: `scale(${scale})`, opacity }}>
    <defs>
      <radialGradient id="koiGlow">
        <stop offset="0%" stopColor={PALETTE.koi} stopOpacity={0.26} />
        <stop offset="100%" stopColor={PALETTE.koi} stopOpacity={0} />
      </radialGradient>
    </defs>
    <circle cx={0} cy={0} r={56} fill="url(#koiGlow)" />
    {/* body */}
    <path d="M -30 0 C -18 -20, 18 -22, 34 0 C 18 22, -18 20, -30 0 Z" fill={PALETTE.koi} />
    {/* tail */}
    <path d="M -30 0 L -52 -17 L -44 0 L -52 17 Z" fill={PALETTE.koi} opacity={0.8} />
    {/* pale saddles */}
    <ellipse cx={8} cy={-3} rx={11} ry={7} fill={PALETTE.ivory} opacity={0.92} />
    <ellipse cx={-13} cy={3} rx={8} ry={5} fill={PALETTE.ivory} opacity={0.85} />
    <circle cx={27} cy={-3} r={2.6} fill="#10151f" />
  </svg>
);

/** The checkerboard that means "no background", the way any image editor shows it. */
const Checker: React.FC<{ size: number }> = ({ size }) => (
  <svg width={size} height={size} style={{ position: "absolute", inset: 0, borderRadius: 22 }}>
    <defs>
      <pattern id="checker" width={22} height={22} patternUnits="userSpaceOnUse">
        <rect width={22} height={22} fill="rgba(255,255,255,0.045)" />
        <rect width={11} height={11} fill="rgba(255,255,255,0.085)" />
        <rect x={11} y={11} width={11} height={11} fill="rgba(255,255,255,0.085)" />
      </pattern>
    </defs>
    <rect width={size} height={size} fill="url(#checker)" rx={22} />
  </svg>
);

const Chip: React.FC<{ label: string; active: boolean; appear: number }> = ({ label, active, appear }) => (
  <div
    style={{
      padding: "11px 20px",
      borderRadius: 999,
      fontSize: 22,
      fontFamily: HAN,
      whiteSpace: "nowrap",
      color: active ? PALETTE.text : PALETTE.muted,
      border: `1px solid ${active ? "rgba(255,81,54,0.6)" : PALETTE.line}`,
      background: active ? "rgba(255,81,54,0.16)" : "rgba(255,255,255,0.035)",
      opacity: appear,
      transform: `translateY(${(1 - appear) * 12}px)`,
    }}
  >
    {label}
  </div>
);

export const Agent: React.FC<{ language: Language }> = ({ language }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const copy = COPY[language];

  const panel = spring({ frame: frame - PANEL_IN, fps, config: { damping: 200 }, durationInFrames: 26 });

  // Typewriter by slicing the string, never by animating per-character opacity.
  const shown = Math.floor(
    interpolate(frame, [TYPE_FROM, TYPE_TO], [0, copy.reply.length], clamp)
  );
  const draft = copy.reply.slice(0, shown);
  const inserted = frame >= INSERTED;

  const stickerPhase = interpolate(frame, [STICKER_FROM, STICKER_TO], [0, 1], clamp);
  const stickerScale = interpolate(stickerPhase, [0, 1], [0.72, 1], {
    ...clamp,
    easing: (t) => 1 - Math.pow(1 - t, 3),
  });

  // The counter moves by the real amounts: a reply costs 1, a sticker costs 6.
  const credits = 250 - (inserted ? 1 : 0) - (stickerPhase > 0.55 ? 6 : 0);

  const activeMode =
    frame >= STICKER_PICKED ? 4 : frame >= REPLY_PICKED ? 2 : -1;

  const fade = interpolate(frame, [HOLD_UNTIL, HOLD_UNTIL + 12], [1, 0], clamp);

  return (
    <AbsoluteFill
      style={{
        background:
          "radial-gradient(1100px 640px at 20% -10%, rgba(93,217,200,0.12), transparent 66%)," +
          "radial-gradient(900px 600px at 88% 10%, rgba(255,81,54,0.14), transparent 68%)," +
          "linear-gradient(180deg,#0a1220 0%,#06070c 62%)",
        alignItems: "center",
        justifyContent: "center",
        opacity: fade,
      }}
    >
      <div style={{ width: 980, display: "grid", gap: 20 }}>
        {/* The conversation you are replying to */}
        <div style={{ display: "grid", gap: 14 }}>
          <div
            style={{
              alignSelf: "start",
              maxWidth: 560,
              padding: "20px 26px",
              borderRadius: "22px 22px 22px 6px",
              background: "rgba(255,255,255,0.07)",
              border: `1px solid ${PALETTE.line}`,
              color: PALETTE.text,
              fontSize: 30,
              fontFamily: HAN,
              opacity: interpolate(frame, [4, 18], [0, 1], clamp),
              transform: `translateY(${interpolate(frame, [4, 18], [14, 0], clamp)}px)`,
            }}
          >
            {copy.incoming}
          </div>

          {inserted ? (
            <div
              style={{
                alignSelf: "end",
                maxWidth: 640,
                padding: "20px 26px",
                borderRadius: "22px 22px 6px 22px",
                background: "rgba(255,81,54,0.18)",
                border: "1px solid rgba(255,81,54,0.42)",
                color: PALETTE.text,
                fontSize: 30,
                fontFamily: HAN,
                opacity: interpolate(frame, [INSERTED, INSERTED + 10], [0, 1], clamp),
                transform: `translateY(${interpolate(frame, [INSERTED, INSERTED + 10], [12, 0], clamp)}px)`,
              }}
            >
              {copy.reply}
            </div>
          ) : null}
        </div>

        {/* The Agent console, where the keyboard would be */}
        <div
          style={{
            padding: 30,
            borderRadius: 30,
            border: `1px solid ${PALETTE.line}`,
            background: "rgba(6,10,18,0.72)",
            boxShadow: "0 44px 100px rgba(0,0,0,0.6)",
            opacity: panel,
            transform: `translateY(${(1 - panel) * 40}px)`,
          }}
        >
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 22 }}>
            <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
              {copy.modes.map((mode, index) => (
                <Chip
                  key={mode}
                  label={mode}
                  active={index === activeMode}
                  appear={interpolate(frame, [PANEL_IN + 6 + index * 3, PANEL_IN + 16 + index * 3], [0, 1], clamp)}
                />
              ))}
            </div>
            <div style={{ textAlign: "right", opacity: panel }}>
              <div style={{ color: PALETTE.dim, fontSize: 15, letterSpacing: "0.14em", textTransform: "uppercase" }}>
                {copy.credits}
              </div>
              <div style={{ color: PALETTE.text, fontSize: 30, fontVariantNumeric: "tabular-nums" }}>{credits}</div>
            </div>
          </div>

          {/* Result area: the drafted reply, then the sticker */}
          <div
            style={{
              position: "relative",
              minHeight: 250,
              borderRadius: 22,
              border: `1px solid ${PALETTE.line}`,
              background: "rgba(255,255,255,0.03)",
              display: "grid",
              placeItems: "center",
              padding: 26,
            }}
          >
            {frame < STICKER_PICKED ? (
              <div style={{ width: "100%" }}>
                <div style={{ color: PALETTE.dim, fontSize: 17, fontFamily: HAN, marginBottom: 14 }}>
                  {shown < copy.reply.length ? `${copy.drafting}…` : copy.replyCost}
                </div>
                <div style={{ color: PALETTE.text, fontSize: 30, lineHeight: 1.55, fontFamily: HAN }}>
                  {draft}
                  {shown < copy.reply.length ? (
                    <span style={{ color: PALETTE.jade }}>▍</span>
                  ) : null}
                </div>
              </div>
            ) : (
              <div style={{ display: "grid", justifyItems: "center", gap: 14 }}>
                {/* The checkerboard is the sticker's own backdrop, so it has to
                    be a box the sticker sits inside — pinned to the whole result
                    area it just lands in a corner beside it. */}
                <div
                  style={{
                    position: "relative",
                    width: 240,
                    height: 240,
                    borderRadius: 22,
                    overflow: "hidden",
                    display: "grid",
                    placeItems: "center",
                  }}
                >
                  <Checker size={240} />
                  <div style={{ position: "relative", display: "grid", placeItems: "center" }}>
                    <KoiSticker
                      scale={stickerScale}
                      opacity={interpolate(stickerPhase, [0, 0.45], [0, 1], clamp)}
                    />
                  </div>
                </div>
                <div
                  style={{
                    color: PALETTE.dim,
                    fontSize: 16,
                    fontFamily: HAN,
                    opacity: interpolate(stickerPhase, [0.6, 1], [0, 1], clamp),
                  }}
                >
                  {copy.transparent} · {copy.stickerCost}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
