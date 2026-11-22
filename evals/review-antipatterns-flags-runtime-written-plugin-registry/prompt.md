---
name: review-antipatterns-flags-runtime-written-plugin-registry
description: >-
  review-antipatterns must flag the module-level `_PLUGINS` dict of
  fixtures/storefront/registry.py as mutable global state at `medium`: it
  looks like a plugin system's registry (filled by a decorator at import
  time), but it is hand-rolled and rewritten at runtime from
  fixtures/storefront/admin.py and fixtures/storefront/tenants.py, so the
  plugin-system exemption does not apply
tags: [review-antipatterns, recall, exemption]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-antipatterns` sub-agent (Agent tool, `subagent_type: "vibe:review-antipatterns"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

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

Once the sub-agent returns, report its findings back verbatim.
