---
name: auto-leaves-no-trace-on-drained-backlog
description: >-
  vibe:auto starts fresh (no .vibe/auto-state.md) on a backlog where 003 is
  blocked and 004 depends on 003: nothing is eligible, so it must not write
  the state file, commit, or dispatch any sub-agent — only report why there
  was nothing to do. No sub-agent runs when the skill behaves, so it keeps
  the usual 3 runs.
tags: [auto, empty-backlog, unattended]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:auto` skill (Skill tool, `skill: "vibe:auto"`) with no argument.

Let it run to completion, including any sub-agent it dispatches. Report its status lines and closing report back verbatim.
