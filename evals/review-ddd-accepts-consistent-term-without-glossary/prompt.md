---
name: review-ddd-accepts-consistent-term-without-glossary
description: >-
  review-ddd, with no .vibe/, no glossary and a README that defines no
  vocabulary, must raise no high or medium Ubiquitous language finding on
  `Batch` — the one name fixtures/logistics/, fixtures/api/ and
  fixtures/reports/ all use — for sounding technical or for a word the
  reviewer would prefer, nor a Value object finding on the bare `carrier`
  string and `weight_grams` integer of fixtures/logistics/batch.py
tags: [review-ddd, precision, glossary]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-ddd` sub-agent (Agent tool, `subagent_type: "vibe:review-ddd"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

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
