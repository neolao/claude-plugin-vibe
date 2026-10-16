---
name: auto-restarts-after-abort-once-a-commit-landed
description: >-
  vibe:auto finds `.vibe/auto-state.md` at `status: stopped` after a run that
  aborted on a broken build, but a later commit repaired it: it must start a
  new run, pick 003 (004 waits on it), ship it through one general-purpose
  sub-agent, honor the limit of 1, append a new journal section while keeping
  the aborted one, and close idle. Deliberately runs 1 (not the usual 3)
  given the cost of a full autonomous cycle.
tags: [auto, abort, precision]
runs: 1
max_turns: 80
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:auto` skill (Skill tool, `skill: "vibe:auto"`) with argument `1`.

The working directory holds the state an earlier run left behind: `.vibe/auto-state.md` says `status: stopped`. Do not tidy any of it up yourself — the skill's own Step 0 decides what to do with that state.

Let it run to completion, including every sub-agent it dispatches. Report its status lines and closing report back verbatim.
