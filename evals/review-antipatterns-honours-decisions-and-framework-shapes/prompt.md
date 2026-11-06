---
name: review-antipatterns-honours-decisions-and-framework-shapes
description: >-
  review-antipatterns must not flag the import-time handler registry of
  fixtures/shop/handlers/ as mutable global state (the repo's
  `.vibe/decisions/001-import-time-handler-registry.md`, status accepted,
  mandates it), the Django settings keys of fixtures/shop/settings.py as
  cargo cult (Django reads them, no repo code does), the primitive columns
  of the `Order` model in fixtures/shop/models.py as primitive obsession
  (the ORM requires them), or `setUp` in
  fixtures/shop/tests/test_dispatch.py as temporal coupling (the test
  framework calls it)
tags: [review-antipatterns, precision, decisions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-antipatterns` sub-agent (Agent tool, `subagent_type: "vibe:review-antipatterns"`) to review `fixtures/` in this case directory. `.vibe/` is present at the workspace root, as it is when `/vibe:feature` runs the review for real. Give it exactly this prompt:

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
