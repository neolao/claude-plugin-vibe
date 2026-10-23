---
name: next-task-auto-mode-ships-the-pick-unattended
description: >-
  vibe:next-task in auto mode, mono-repo scope, must hand its pick (001, a
  defect) to vibe:fix with --auto itself — no confirmation, no vibe:auto —
  then invoke vibe:publish and end on a report naming the push failure as a
  blocker, never on a question. Runs a real, trivial vibe:fix cycle.
  Requires `--allow-tools Bash,Write,Edit` to run.
tags: [next-task, mono-repo, auto-mode, unattended, precision]
runs: 1
max_turns: 80
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

You are in a mono-repo (no workspace hub, just this repo's own `.vibe/backlog/`) with two backlog items. Everything is already set up — do not create, edit, or commit anything yourself before invoking the skill.

Invoke the `vibe:next-task` skill (Skill tool, `skill: "vibe:next-task"`) with `auto 1` as `$ARGUMENTS` — the autonomous mode, where it picks, hands off and publishes with no confirmation.

Nobody is available to reply during this run: if anything asks you a question, do not answer it and do not end your turn on it — the skill is expected to need no answer. Let it run to completion. The repo has no Git remote on purpose: the push is expected to fail with a Git error, which the skill reports as a blocker — do not add a remote, do not force-push, do not treat it as a success.

Once `vibe:next-task`'s final report comes back, report it back verbatim.
