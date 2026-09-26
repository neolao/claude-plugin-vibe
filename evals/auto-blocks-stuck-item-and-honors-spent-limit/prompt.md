---
name: auto-blocks-stuck-item-and-honors-spent-limit
description: >-
  vibe:auto resumes a run whose current item 003 is still in_progress at
  attempt 2 with uncommitted partial work: it must commit that work as
  `wip: resume auto run (item 003)`, mark 003 blocked, journal it, and — the
  run's limit of 3 now being spent by 001, 002 and 003 — close the run without
  starting 004, although 004 is eligible. No sub-agent runs when the skill
  behaves, so unlike its sibling auto cases it keeps the usual 3 runs.
tags: [auto, resume, limit]
runs: 3
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit]
---

Invoke the `vibe:auto` skill (Skill tool, `skill: "vibe:auto"`) with no argument.

The working directory already holds an interrupted run: `.vibe/auto-state.md` says `status: running` with `current: 003`, and the working tree has uncommitted changes. Do not tidy any of it up yourself — the skill's own Step 0 decides what to do with that state.

Let it run to completion, including any sub-agent it dispatches. Report its status lines and closing report back verbatim.
