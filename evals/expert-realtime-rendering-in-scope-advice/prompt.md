---
name: expert-realtime-rendering-in-scope-advice
description: expert-realtime-rendering must surface per-frame allocation, blocking-load, and fixed-timestep pitfalls for a particle-highlight brief
tags: [expert-realtime-rendering, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-realtime-rendering` sub-agent (Agent tool, `subagent_type: "vibe:expert-realtime-rendering"`) with this plan consultation.

Give it exactly this message:

```
Brief: in the 3D editor's viewport, whenever an object is selected we want a
sparkle-particle highlight around it, driven by a lightweight physics
simulation (particles drift and settle under a simple gravity/drag model) so
the effect reads the same whether the editor is running at 30 fps on a laptop
or 144 fps on a gaming monitor. On first selection of an object, if its
sparkle texture isn't loaded yet we'll load it from disk right then so the
effect can start immediately. Each selected object spawns its own small burst
of particle instances every frame while selected. Target platforms include
older integrated-GPU laptops, so we want this to stay smooth even with
several objects selected at once.

Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Once the sub-agent returns, report its reply back verbatim.
