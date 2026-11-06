---
name: expert-architecture-neighbours-reversed-dependency-stays-a-defect
description: >-
  Recall of the hard-defect floor under the idiom rule: the two existing
  features that save a file both import the S3 adapter directly from
  `core/`, against the module map (core depends on nothing) and the
  recorded decision that dependencies point inward. A third feature of the
  same kind is requested and the brief invites copying the neighbours. The
  expert must name that import as a reversed dependency — a defect, not
  the idiom to follow — and recommend an option that keeps the new code in
  core behind a port or an injected dependency.
tags: [expert-architecture, recall, idiom-floor]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-architecture` sub-agent (Agent tool, `subagent_type: "vibe:expert-architecture"`) with this brief, the plan notes and the consultation request below. The code is in `fixtures/` of this case directory and `.vibe/` is present at the workspace root, as it is when `/vibe:feature` consults the expert for real.

Brief:

```
We're adding monthly statements to our billing service: once a month, for
each account, build the statement from the account's invoices of the month
and save the file to S3 where the customer portal picks it up. Invoices and
CSV exports are already built in core and saved to S3 the same way, so the
obvious thing is to do like those two. Is there a better way to shape it?
```

Plan notes (send after the brief):

```
The code is in `fixtures/` of the working directory: package `core/`
(invoice and export services, pricing), package `adapters/` (S3 storage,
Postgres repository) and `app.py` (routes and composition root). `.vibe/`
at the workspace root holds the module map and the decisions.
```

Consultation request (send verbatim, appended to the notes):

```
Reply, in place of the usual three lists, with: BASELINE: (the obvious approach a competent developer writes, named, against the real files, with its cost and weak criteria), ALTERNATIVES: (up to two named patterns, each scored against the baseline on an explicit grid with a BETTER / TIE / WORSE verdict and the count of criteria won and lost), RECOMMENDATION: (one option, justified by the constraints). Add OPEN QUESTIONS: (≤3) only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
