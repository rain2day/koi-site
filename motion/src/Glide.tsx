/* One stroke, one character — as a film.
 *
 * The interactive demo lower down the page asks the visitor to do something.
 * Plenty of them will not, and a keyboard that is never touched explains
 * nothing. This runs the same stroke by itself, once, in about five seconds:
 * the finger leaves h, crosses g, f and s on its way to a, and 香 lands.
 *
 * Every frame is a function of `useCurrentFrame()`. There is no CSS transition
 * anywhere in this file — Remotion renders frames out of order, so anything
 * driven by wall-clock time would tear.
 */

import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import {
  BOARD_HEIGHT,
  BOARD_WIDTH,
  CANDIDATES,
  CROSSED,
  INTENDED,
  KEYS,
  PALETTE,
  RADICALS,
  centreOf,
  crossingProgress,
  pointAlong,
} from "./keyboard";

// Beats, in frames at 30fps.
const SETTLE = 12;
const STROKE_START = 26;
const STROKE_END = 78;
const CANDIDATES_AT = 84;
const COMMIT_AT = 104;
const HOLD_UNTIL = 138;

const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

const Key: React.FC<{ letter: string; x: number; y: number; width: number; height: number; progress: number }> = ({
  letter,
  x,
  y,
  width,
  height,
  progress,
}) => {
  const crossed = CROSSED.includes(letter);
  const touchedAt = crossed ? crossingProgress(letter) : 2;
  // A key lights when the finger reaches it and cools shortly after, so the
  // stroke leaves a wake rather than turning the whole row on at once.
  const since = progress - touchedAt;
  const heat = crossed && since >= 0 ? interpolate(since, [0, 0.28], [1, 0], clamp) : 0;
  const wanted = INTENDED.has(letter);
  const tint = wanted ? PALETTE.koi : PALETTE.jade;

  return (
    <g>
      <rect
        x={x}
        y={y}
        width={width}
        height={height}
        rx={12}
        fill={`rgba(255,255,255,${0.055 + heat * 0.1})`}
        stroke={heat > 0.02 ? tint : PALETTE.line}
        strokeWidth={heat > 0.02 ? 1.5 : 1}
        opacity={heat > 0.02 ? 0.55 + heat * 0.45 : 1}
      />
      <text
        x={x + 9}
        y={y + 21}
        fill={PALETTE.muted}
        fontSize={17}
        fontFamily="'PingFang HK','Noto Sans HK',sans-serif"
      >
        {RADICALS[letter]}
      </text>
      <text
        x={x + width / 2}
        y={y + height / 2 + 14}
        fill={PALETTE.text}
        fontSize={31}
        textAnchor="middle"
        fontFamily="ui-sans-serif,-apple-system,sans-serif"
      >
        {letter}
      </text>
    </g>
  );
};

const Trail: React.FC<{ progress: number }> = ({ progress }) => {
  if (progress <= 0) return null;

  // Sampled rather than drawn as a two-point line, so the ribbon can taper and
  // the corner at d is rounded the way a finger actually turns.
  const samples = 60;
  const points = Array.from({ length: samples + 1 }, (_, index) =>
    pointAlong((index / samples) * progress)
  );

  const tail = pointAlong(0);
  const head = pointAlong(progress);

  return (
    <g>
      <defs>
        {/* userSpaceOnUse, not the default objectBoundingBox. h, d and a all sit
            on the home row, so this stroke is perfectly horizontal and its
            bounding box has zero height — under bounding-box units an SVG
            gradient and filter over a degenerate box are undefined, and the
            renderer drops them, taking the whole ribbon with them. Explicit
            user-space coordinates also fix the gradient's direction: the stroke
            travels right to left, so tail→head is not left→right. */}
        <linearGradient
          id="trail"
          gradientUnits="userSpaceOnUse"
          x1={tail.x}
          y1={tail.y}
          x2={head.x}
          y2={head.y}
        >
          <stop offset="0%" stopColor={PALETTE.jade} stopOpacity={0.06} />
          <stop offset="36%" stopColor={PALETTE.jade} stopOpacity={0.6} />
          <stop offset="76%" stopColor={PALETTE.ivory} stopOpacity={0.9} />
          <stop offset="100%" stopColor={PALETTE.lagoon} stopOpacity={0.6} />
        </linearGradient>
        <filter
          id="glow"
          filterUnits="userSpaceOnUse"
          x={-60}
          y={-60}
          width={BOARD_WIDTH + 120}
          height={BOARD_HEIGHT + 120}
        >
          <feGaussianBlur stdDeviation="7" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>

      <polyline
        points={points.map((point) => `${point.x},${point.y}`).join(" ")}
        fill="none"
        stroke="url(#trail)"
        strokeWidth={13}
        strokeLinecap="round"
        strokeLinejoin="round"
        filter="url(#glow)"
        opacity={0.95}
      />

      {(() => {
        return (
          <>
            <circle cx={head.x} cy={head.y} r={26} fill={PALETTE.jade} opacity={0.14} />
            <circle cx={head.x} cy={head.y} r={11} fill={PALETTE.ivory} opacity={0.92} />
          </>
        );
      })()}
    </g>
  );
};

export const Glide: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const settle = spring({ frame, fps, config: { damping: 200 }, durationInFrames: SETTLE * 2 });
  const progress = interpolate(frame, [STROKE_START, STROKE_END], [0, 1], clamp);
  const committed = frame >= COMMIT_AT;

  // The composing radicals appear as the finger passes the keys it meant.
  const composed = ["h", "d", "a"]
    .filter((letter) => progress >= crossingProgress(letter) - 0.02)
    .map((letter) => RADICALS[letter])
    .join("");

  const fade = interpolate(frame, [HOLD_UNTIL, HOLD_UNTIL + 10], [1, 0], clamp);

  return (
    <AbsoluteFill
      style={{
        background:
          "radial-gradient(1200px 700px at 76% -10%, rgba(255,81,54,0.16), transparent 68%)," +
          "radial-gradient(900px 620px at 8% 8%, rgba(93,217,200,0.10), transparent 66%)," +
          "linear-gradient(180deg,#0a1220 0%,#06070c 60%)",
        alignItems: "center",
        justifyContent: "center",
        opacity: fade,
      }}
    >
      <div
        style={{
          width: BOARD_WIDTH + 96,
          padding: 48,
          borderRadius: 34,
          border: `1px solid ${PALETTE.line}`,
          background: "rgba(6,10,18,0.62)",
          boxShadow: "0 50px 110px rgba(0,0,0,0.6)",
          transform: `translateY(${(1 - settle) * 28}px)`,
          opacity: settle,
        }}
      >
        {/* Text field */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            minHeight: 82,
            padding: "0 26px",
            borderRadius: 18,
            border: `1px solid ${PALETTE.line}`,
            background: "rgba(255,255,255,0.045)",
            fontSize: 40,
            color: PALETTE.text,
            fontFamily: "'PingFang HK','Noto Sans HK',sans-serif",
          }}
        >
          {committed ? (
            <span>香</span>
          ) : composed ? (
            <span style={{ color: "#FF7A63", textDecoration: "underline", textUnderlineOffset: 8 }}>
              {composed}
            </span>
          ) : (
            <span style={{ color: PALETTE.dim, fontSize: 26 }}>在此試打</span>
          )}
        </div>

        {/* Candidate row: numbers until a composition starts, exactly as on the device */}
        <div
          style={{
            display: "flex",
            gap: 8,
            minHeight: 74,
            marginTop: 16,
            padding: 8,
            borderRadius: 16,
            background: "rgba(255,255,255,0.03)",
            alignItems: "stretch",
          }}
        >
          {frame < CANDIDATES_AT
            ? "1234567890".split("").map((digit) => (
                <div
                  key={digit}
                  style={{
                    flex: 1,
                    display: "grid",
                    placeItems: "center",
                    color: PALETTE.dim,
                    fontSize: 24,
                  }}
                >
                  {digit}
                </div>
              ))
            : CANDIDATES.map((character, index) => {
                const appear = interpolate(frame, [CANDIDATES_AT + index * 2, CANDIDATES_AT + index * 2 + 8], [0, 1], clamp);
                const chosen = committed && index === 0;
                return (
                  <div
                    key={character}
                    style={{
                      display: "flex",
                      alignItems: "baseline",
                      gap: 7,
                      padding: "8px 16px",
                      borderRadius: 12,
                      border: `1px solid ${chosen ? "rgba(255,81,54,0.55)" : "transparent"}`,
                      background: index === 0 ? "rgba(255,81,54,0.13)" : "transparent",
                      opacity: appear,
                      transform: `translateY(${(1 - appear) * 10}px)`,
                    }}
                  >
                    <span style={{ color: PALETTE.dim, fontSize: 15 }}>{index + 1}</span>
                    <span
                      style={{
                        color: PALETTE.text,
                        fontSize: 34,
                        fontFamily: "'PingFang HK','Noto Sans HK',sans-serif",
                      }}
                    >
                      {character}
                    </span>
                  </div>
                );
              })}
        </div>

        {/* The keyboard, with the stroke drawn over it */}
        <svg
          width={BOARD_WIDTH}
          height={BOARD_HEIGHT}
          viewBox={`0 0 ${BOARD_WIDTH} ${BOARD_HEIGHT}`}
          style={{ display: "block", marginTop: 22 }}
        >
          {KEYS.map((key) => (
            <Key key={key.letter} {...key} progress={progress} />
          ))}
          <Trail progress={progress} />
        </svg>
      </div>
    </AbsoluteFill>
  );
};
