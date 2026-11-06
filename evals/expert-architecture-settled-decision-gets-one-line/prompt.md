---
name: expert-architecture-settled-decision-gets-one-line
description: >-
  Recall of the settled-choice rule of expert-architecture: the repo's
  `.vibe/decisions/001-channel-registry.md` already decides how a delivery
  channel is added (one adapter module registered by name in the core
  registry, nothing in core touched) and the two existing channels follow
  it. A third channel is requested. The expert must read `.vibe/` and reply
  in one line naming the decision or the registry, instead of filling the
  requested format with a baseline, scored alternatives and a recommendation
  for a choice that is not open.
tags: [expert-architecture, recall, settled-decision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-architecture` sub-agent (Agent tool, `subagent_type: "vibe:expert-architecture"`) with this brief, the plan notes and the consultation request below. The code is in `fixtures/` of this case directory and `.vibe/` is present at the workspace root, as it is when `/vibe:feature` consults the expert for real.

Brief:

```
Our notification service sends email and push. We're adding SMS through
Twilio as a third channel: a message says which channel it wants, and the
service must send it through Twilio when it says "sms". Where should the
Twilio-specific code live, and how should the service pick SMS at runtime?
We can see several ways to do it.
```

Plan notes (send after the brief):

```
The code is in `fixtures/` of the working directory: package `core/`
(message, router) and package `adapters/notify/` (one module per channel).
`.vibe/` at the workspace root holds the module map and the decisions.
```

Consultation request (send verbatim, appended to the notes):

```
Reply, in place of the usual three lists, with: BASELINE: (the obvious approach a competent developer writes, named, against the real files, with its cost and weak criteria), ALTERNATIVES: (up to two named patterns, each scored against the baseline on an explicit grid with a BETTER / TIE / WORSE verdict and the count of criteria won and lost), RECOMMENDATION: (one option, justified by the constraints). Add OPEN QUESTIONS: (≤3) only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
