---
name: expert-architecture-local-idiom-beats-textbook-pattern
description: >-
  Precision side of the idiom rule: a small reporting tool selects its
  output format through a dict of plain functions, which is not the
  textbook Strategy hierarchy, breaks no layering (the tool has none) and
  contradicts no decision. A third format is requested and the brief asks
  whether it is time for a base class. The expert must follow the function
  registry — as the idiom that settles the form, or as the winning
  baseline — and not prescribe a class hierarchy, a package split or a
  migration of the two existing formats.
tags: [expert-architecture, precision, idiom-floor]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-architecture` sub-agent (Agent tool, `subagent_type: "vibe:expert-architecture"`) with this brief, the plan notes and the consultation request below. The code is in `fixtures/` of this case directory; the project has no `.vibe/`.

Brief:

```
Our `reportkit` command renders a table as CSV or JSON, picked with
`--format`. We're adding a Markdown output (a GitHub-style table). Now that
there are three formats, should we introduce a proper Formatter base class
with one subclass per format, or a `formats/` package with one module each,
or something else? Or is that overkill?
```

Plan notes (send after the brief):

```
The code is in `fixtures/` of the working directory: package `reportkit/`
(`table.py`, `formats.py`, `cli.py`). The project has no `.vibe/`.
```

Consultation request (send verbatim, appended to the notes):

```
Reply, in place of the usual three lists, with: BASELINE: (the obvious approach a competent developer writes, named, against the real files, with its cost and weak criteria), ALTERNATIVES: (up to two named patterns, each scored against the baseline on an explicit grid with a BETTER / TIE / WORSE verdict and the count of criteria won and lost), RECOMMENDATION: (one option, justified by the constraints). Add OPEN QUESTIONS: (≤3) only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
