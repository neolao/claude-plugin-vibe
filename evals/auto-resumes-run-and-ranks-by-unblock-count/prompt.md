---
name: auto-resumes-run-and-ranks-by-unblock-count
description: >-
  vibe:auto must resume an interrupted run (journal 002 as done since it is
  already under done/, reset the orphaned in_progress 006 to todo) and then
  pick 004 — the item 005 waits on — ahead of the lower-numbered defect 003.
  Deliberately runs 1 (not the usual 3) given the cost of a full autonomous
  cycle. Requires `--allow-tools Bash,Write,Edit` to run.
tags: [auto, resume, ranking]
runs: 1
max_turns: 80
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit]
---

Invoke the `vibe:auto` skill (Skill tool, `skill: "vibe:auto"`) with no argument.

The working directory already holds an interrupted run: `.vibe/auto-state.md` says `status: running` with `current: 002`, and a backlog with several items. Do not tidy any of it up yourself — the skill's own Step 0 decides what to do with that state.

Let it run to completion, including every sub-agent it dispatches. Report its status lines and closing report back verbatim.
