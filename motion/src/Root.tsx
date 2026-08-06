import React from "react";
import { Composition } from "remotion";
import { Glide } from "./Glide";
import { Agent } from "./Agent";

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="Glide" component={Glide} durationInFrames={150} fps={30} width={1280} height={860} />
    {/* One film per language: the Agent one carries real sentences, so it cannot
        be language-neutral the way the glide film is. */}
    <Composition
      id="AgentZh"
      component={Agent}
      defaultProps={{ language: "zh" as const }}
      durationInFrames={282}
      fps={30}
      width={1280}
      height={860}
    />
    <Composition
      id="AgentEn"
      component={Agent}
      defaultProps={{ language: "en" as const }}
      durationInFrames={282}
      fps={30}
      width={1280}
      height={860}
    />
  </>
);
