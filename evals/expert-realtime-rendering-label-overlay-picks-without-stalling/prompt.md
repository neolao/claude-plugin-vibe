---
name: expert-realtime-rendering-label-overlay-picks-without-stalling
description: >-
  A viewport that draws a name label above every object and finds the object
  under the cursor on each mouse move is a render-loop brief: the expert must
  require the labels to share draw submission instead of one draw per label,
  keep the cursor lookup from reading the frame back to the CPU in the middle
  of the frame, state a numeric frame budget, and keep its open questions to
  business choices.
tags: [expert-realtime-rendering, recall, batching, readback]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-realtime-rendering` sub-agent (Agent tool, `subagent_type: "vibe:expert-realtime-rendering"`) with this brief plus the consultation request below.

Brief:

```
The 3D editor's viewport must show the name of every object of the scene as
a text label floating above it, so designers can read the scene at a glance;
scenes go up to 1,500 objects. The plan: each label is its own small textured
quad, drawn with its own draw call right after its object, using the label's
texture. Hovering is also changing: today the object under the cursor is
found with a CPU ray test; we'd like to switch to rendering the scene once
with a flat colour per object and reading back the pixel under the cursor,
run on every mouse move, so the result is pixel-exact even for thin objects.
The editor runs in the browser (WebGL) and the target is a 60 fps viewport on
mid-range laptops.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
