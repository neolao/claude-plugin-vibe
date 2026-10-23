---
name: next-task-auto-mode-skips-a-cross-repo-blocked-item
description: >-
  vibe:next-task in auto mode must hand its own pick (orders-api 002, the
  only item not blocked across repos) to vibe:fix with --auto, never hand
  the repo to vibe:auto, never start orders-api 001, then invoke
  vibe:publish and report the push failure as a blocker. Runs a real,
  trivial vibe:fix cycle. Requires `--allow-tools Bash,Write,Edit` to run.
tags: [next-task, workspace, auto-mode, unattended]
runs: 1
max_turns: 80
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

You are at the root of a workspace: a hub repo plus two active sibling repos, each with its own backlog. Everything is already set up — do not create, edit, or commit anything yourself before invoking the skill.

Invoke the `vibe:next-task` skill (Skill tool, `skill: "vibe:next-task"`) with `auto 1` as `$ARGUMENTS` — the autonomous mode, where it picks, hands off and publishes with no confirmation.

Nobody is available to reply during this run: if anything asks you a question, do not answer it and do not end your turn on it — the skill is expected to need no answer. Let it run to completion. The repos have no Git remote on purpose: the push is expected to fail with a Git error, which the skill reports as a blocker — do not add a remote, do not force-push, do not treat it as a success.

Once `vibe:next-task`'s final report comes back, report it back verbatim.
