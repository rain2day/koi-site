import React from "react";
import { Composition } from "remotion";
import { Glide } from "./Glide";

export const RemotionRoot: React.FC = () => (
  <Composition
    id="Glide"
    component={Glide}
    durationInFrames={150}
    fps={30}
    width={1280}
    height={860}
  />
);
