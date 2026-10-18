---
name: clarify-implementation-mode-reads-the-code-first
description: >
  clarify in `mode: implementation` must settle every technical decision
  from the code and CLAUDE.md — a new `Exporter` subclass registered in
  `exports/__init__.py`, unittest under `tests/`, cents formatted in the
  exporter — each with its source, through a dispatched sub-agent, ask the
  Product Owner nothing (AskUserQuestion is granted and must stay unused),
  and end with `CLARIFY-RESULT: settled — mode: implementation` without
  reopening what the product does. Needs --allow-tools AskUserQuestion to
  run.
tags: [clarify, implementation-mode]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Agent, AskUserQuestion]
---

You are the build workflow of `vibe:feature`. The need is settled; you now frame the implementation. Invoke the `vibe:clarify` skill (Skill tool, `skill: "vibe:clarify"`) with this argument, verbatim:

```
mode: implementation
Need, settled: admins (owner role only) download the monthly report as a CSV file — one line per transaction with date, amount and label — for a month they pick, the current month by default; a month with no transaction gives a header-only file.
Expert consultation: none (no expert matched this brief).
```

The current directory is the project (code in `exports/`, tests in `tests/`, conventions in `CLAUDE.md`).

If `vibe:clarify` asks a round of questions, answer decisively yourself without waiting. In your final message, reproduce `vibe:clarify`'s entire run verbatim: every round it asked (if any), your answers, and its closing report (the `CLARIFY-RESULT:` line and everything under it).
