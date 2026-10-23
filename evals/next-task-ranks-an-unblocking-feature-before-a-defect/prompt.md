---
name: next-task-ranks-an-unblocking-feature-before-a-defect
description: >-
  vibe:next-task in mono-repo scope must pick the feature 001, which item
  003 depends on, over the defect 002, which nothing waits on: the unblock
  count comes before defects-first. Stopped at the Step 6 confirmation.
  Requires `--allow-tools Bash` to run.
tags: [next-task, mono-repo, scoring, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

Invoke the `vibe:next-task` skill (Skill tool, `skill: "vibe:next-task"`) with an empty argument — the normal mode, where it picks a candidate itself and asks you to confirm before doing anything.

You are in a mono-repo (no workspace hub, just this repo's own `.vibe/backlog/`). Everything is already set up — do not create, edit, or commit anything yourself.

When the skill presents its pick and asks for confirmation, **decline**: tell it plainly, in your own words, that you do not want to start that work now. Do not approve, do not ask it to pick something else, and do not start any implementation yourself.

In your final message, reproduce the skill's pick presentation verbatim — the item it chose, its reasoning, and anything it said about the items it did not choose.
