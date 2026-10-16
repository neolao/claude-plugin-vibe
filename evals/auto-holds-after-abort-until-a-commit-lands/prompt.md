---
name: auto-holds-after-abort-until-a-commit-lands
description: >-
  vibe:auto finds `.vibe/auto-state.md` at `status: stopped` after a run that
  aborted on a broken build; HEAD is still that run's closing commit and the
  tree is clean. It must hold: repeat the journaled reason, start no run,
  dispatch no sub-agent, commit nothing, and leave the state `stopped`. No
  sub-agent runs when the skill behaves, so it keeps the usual 3 runs.
tags: [auto, abort, unattended]
runs: 3
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:auto` skill (Skill tool, `skill: "vibe:auto"`) with no argument.

The working directory holds the state an earlier run left behind: `.vibe/auto-state.md` says `status: stopped`. Do not tidy any of it up yourself, and do not repair anything in the project — the skill's own Step 0 decides what to do with that state.

Let it run to completion, including any sub-agent it dispatches. Report its status lines and closing report back verbatim.
