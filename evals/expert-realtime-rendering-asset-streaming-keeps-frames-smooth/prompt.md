---
name: expert-realtime-rendering-asset-streaming-keeps-frames-smooth
description: >-
  A viewport that streams textures in from the asset service while frames keep
  going is a render-loop brief even though an HTTP service is involved:
  expert-realtime-rendering must answer in the three-list format (not redirect
  it as "an API"), keep the fetch and PNG decode off the loop, keep a large GPU
  texture upload from landing whole in one frame, flag the first-draw shader
  compilation as a stall to warm up at load, state a numeric frame budget
  (16.6 ms at 60 fps, since the brief names no target) — and prescribe nothing
  about the service's HTTP contract.
tags: [expert-realtime-rendering, recall, asset-streaming]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-realtime-rendering` sub-agent (Agent tool, `subagent_type: "vibe:expert-realtime-rendering"`) with this brief plus the consultation request below.

Brief:

```
The 3D editor's viewport shows a product scene built from the catalog's
assets, which the asset service serves over HTTP as PNG textures and glTF
meshes. Today every asset of the scene is downloaded and decoded before the
viewport opens, which takes up to a minute on big scenes. We're changing it
so the viewport opens on low-resolution placeholders and streams the
full-resolution textures in as the camera gets close to an object: the plan
is to fetch the PNG, decode it and create the GPU texture at the moment the
object first comes within range, and the engine compiles that material's
shader the first time the object is drawn. The editor runs in the browser
(WebGL) on the designers' laptops and on the showroom's wall display, and
the camera keeps moving while textures arrive.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
