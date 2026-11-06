---
name: review-comments-rewrites-a-required-docstring
description: >-
  review-comments must report the docstring of the public `parse_amount` in
  fixtures/pricing/amounts.py, which only restates its name, with a
  SUGGESTION that writes its contract (cents returned, comma accepted,
  ValueError on a non-amount or a negative) and never `delete` — the
  fixture's CLAUDE.md and setup.cfg make pydocstyle require it — while the
  docstring of the private `_strip_currency`, exempt from the rule, may be
  deleted
tags: [review-comments, recall]
runs: 3
max_turns: 10
timeout_seconds: 600
allowed_tools: [Read, Grep, Glob, Agent, Bash]
---

Invoke the `vibe:review-comments` sub-agent (Agent tool, `subagent_type: "vibe:review-comments"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

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
