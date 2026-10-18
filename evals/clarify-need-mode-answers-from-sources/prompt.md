---
name: clarify-need-mode-answers-from-sources
description: >
  clarify in `mode: need` must settle from the sources what they answer —
  the export format and the columns (backlog item 007), who "admins" are
  (.vibe/decisions/002: owner role only) — citing each source, dispatch a
  sub-agent to read them rather than reading itself, ask the Product Owner
  only the business decision no source settles (what happens with a month
  that has no transaction), and end with `CLARIFY-RESULT: settled — mode:
  need` without any decision about code or approach. Needs --allow-tools
  AskUserQuestion to run.
tags: [clarify, need-mode]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Agent, AskUserQuestion]
---

You are the build workflow of `vibe:feature`, framing the need before any plan. Invoke the `vibe:clarify` skill (Skill tool, `skill: "vibe:clarify"`) with this argument, verbatim:

```
mode: need
Backlog item 007 — Export the monthly report (the item file is .vibe/backlog/007-export-monthly-report.md in the current directory).
```

The current directory holds the project's `.vibe/` (index, decisions, backlog). No project memory directory is indicated for this session.

When `vibe:clarify` presents a round of questions in its `❓ **Q1**` / `➡️` format, do not wait for a separate message — answer every question yourself, right away, decisively, as the Product Owner would (for example: a month with no transaction still produces a file with the header line only). If a later round asks anything further, answer it the same way until `vibe:clarify` reaches its end state.

In your final message, reproduce `vibe:clarify`'s entire run verbatim: every round of questions it asked, the answers you gave, and its closing report (the `CLARIFY-RESULT:` line and everything under it).
