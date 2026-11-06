---
name: review-architecture-accepts-a-stale-map
description: >-
  review-architecture must not report a stale `.vibe/` map as drift: a pure
  file the core module's `Files:` list omits (fixtures/core/discounts.py), a
  zone the map has no module for that imports inward only
  (fixtures/notifications/), a mapped module whose listed file no longer
  exists (`reports`), a job nothing imports but that fixtures/pyproject.toml
  declares as a console script (`jobs`), and a glossary concept computed once
  in fixtures/core/pricing.py and referenced from three other modules
tags: [review-architecture, precision, stale-map]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-architecture` sub-agent (Agent tool, `subagent_type: "vibe:review-architecture"`) to review `fixtures/` in this case directory. `.vibe/` is present at the workspace root, as it is when the internal review runs for real. Give it exactly this prompt:

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

Scope: fixtures/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim (or state that it found nothing).
