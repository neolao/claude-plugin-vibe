---
name: review-security-scoped-accepts-evidence-outside-scope
description: >-
  review-security, scoped to fixtures/archiver/lib/, must raise no high or
  medium finding on the helpers in scope (the shell helper of proc.py runs
  gpg on a dated path, the containment check of paths.py receives manifest
  entries validated outside, the unpickler of serializer.py reads the index
  the tool itself wrote, the random id of ids.py labels the restore job
  while the tokens come from `secrets`, the permission table of perms.py
  carries every action the commands check) and must report nothing on the
  concatenated INSERT that sits wholly in fixtures/archiver/store.py
tags: [review-security, precision, scoped]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-security` sub-agent (Agent tool, `subagent_type: "vibe:review-security"`) to review `fixtures/archiver/lib/` in this case directory. Give it exactly this prompt:

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

Scope: fixtures/archiver/lib/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim (or state that it found nothing).
