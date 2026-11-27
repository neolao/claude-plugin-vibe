---
name: review-security-scoped-finds-evidence-outside-scope
description: >-
  review-security, scoped to fixtures/archiver/lib/, must find the shell
  helper of proc.py that the restore command feeds the partner-chosen archive
  name, the containment check of paths.py that lets the partner's manifest
  entries through, the unpickler of serializer.py that reads the partner's
  MANIFEST, the random id of ids.py used as the share token, and the
  permission table of perms.py missing the action restore checks — anchoring
  every finding on a file under fixtures/archiver/lib/ and leaving alone the
  concatenated INSERT that sits wholly in fixtures/archiver/store.py
tags: [review-security, recall, scoped]
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

Once the sub-agent returns, report its findings back verbatim.
