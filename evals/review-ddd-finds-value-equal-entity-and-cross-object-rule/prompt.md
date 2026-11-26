---
name: review-ddd-finds-value-equal-entity-and-cross-object-rule
description: >-
  review-ddd must report `Member` in fixtures/studio/member.py, an entity
  with a `member_id` that the default dataclass equality compares on every
  attribute, as an Entity finding, and the late-cancellation fee that
  `CancelBooking.execute` in fixtures/booking/cancel.py computes from the
  member's tier, the session's start and the clock, as a Domain service
  finding, while leaving the frozen `Slot` and the `AttendanceLine` read
  model, both compared by value on purpose, alone
tags: [review-ddd, recall, entity, domain-service]
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

Once the sub-agent returns, report its findings back verbatim.
