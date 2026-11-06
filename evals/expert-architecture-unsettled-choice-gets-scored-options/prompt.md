---
name: expert-architecture-unsettled-choice-gets-scored-options
description: >-
  Precision side of the settled-choice rule: `.vibe/` decides only the
  layering (ports in core, provider code in adapters) and nothing about how
  a channel is chosen — the second channel was bolted on as an `elif` in the
  core service last quarter. A third channel is a real design choice: the
  expert must not hide behind "the repo prescribes the form" but name the
  baseline against the real files, score at least one named alternative
  with a verdict, and recommend — while keeping the provider SDK out of
  core as the decision requires.
tags: [expert-architecture, precision, settled-decision]
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
service must send it through Twilio when it says "sms". Push was bolted on
as an elif in the core service last quarter and nobody is attached to that
shape. Where should the Twilio-specific code live, and how should the
service pick SMS at runtime? We can see several ways to do it.
```

Plan notes (send after the brief):

```
The code is in `fixtures/` of the working directory: package `core/`
(message, ports, notification service), package `adapters/notify/` (one
class per channel) and `app.py` (composition root). `.vibe/` at the
workspace root holds the module map and the decisions.
```

Consultation request (send verbatim, appended to the notes):

```
Reply, in place of the usual three lists, with: BASELINE: (the obvious approach a competent developer writes, named, against the real files, with its cost and weak criteria), ALTERNATIVES: (up to two named patterns, each scored against the baseline on an explicit grid with a BETTER / TIE / WORSE verdict and the count of criteria won and lost), RECOMMENDATION: (one option, justified by the constraints). Add OPEN QUESTIONS: (≤3) only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
