---
name: review-docs-scoped-finds-evidence-outside-scope
description: >-
  review-docs, scoped to fixtures/docs/guides/, must report the 5 000-row
  cap of fixtures/docs/guides/import.md against the 10 000 rows of
  fixtures/docs/reference/limits.md, the guide fixtures/docs/guides/export.md
  that the index of fixtures/README.md never lists, and the link of
  fixtures/docs/guides/export.md to a reference page that does not exist —
  anchoring every finding on a file under fixtures/docs/guides/ and leaving
  the timeout disagreement between fixtures/docs/reference/cli.md and
  fixtures/docs/reference/limits.md alone
tags: [review-docs, recall, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-docs` sub-agent (Agent tool, `subagent_type: "vibe:review-docs"`) to review `fixtures/docs/guides/` in this case directory. Give it exactly this prompt:

```
Review the code in scope for your dimension only. Read-only: never edit, create, or run anything the agent definition does not explicitly allow.
Report every finding as:

FILE: path/to/file (line N)      — or MODULE:, PACKAGE:, TARGET: when your definition says so
CATEGORY: <one of your categories>
SEVERITY: high | medium | low
ISSUE: what is wrong and why it matters — one or two sentences
SUGGESTION: concrete fix direction — one or two sentences

Severity: high = correctness, security, or a bug that will ship; medium = a clear principle or convention broken; low = minor improvement.
Flag only what you can point to in the code, with a plausible failure or cost — no theoretical findings, no metric-chasing. Skip a category with nothing to report. Do not summarize or count at the end.

Scope: fixtures/docs/guides/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim.
