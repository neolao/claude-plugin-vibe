---
name: next-task-leaves-a-busy-repo-alone
description: >-
  vibe:next-task in workspace scope must leave out billing-api (uncommitted
  change in its working tree) and billing-jobs (an item in progress), name
  both with the reason, and pick billing-web 001 although the items of the
  two busy repos would out-score it. Stopped at the Step 6 confirmation.
  Requires `--allow-tools Bash` to run.
tags: [next-task, workspace, busy-repo]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

Invoke the `vibe:next-task` skill (Skill tool, `skill: "vibe:next-task"`) with an empty argument — the normal mode, where it picks a candidate itself and asks you to confirm before doing anything.

You are at the root of a workspace: a hub repo plus sibling repos, each with its own backlog. Everything is already set up — do not create, edit, or commit anything yourself.

When the skill presents its pick and asks for confirmation, **decline**: tell it plainly, in your own words, that you do not want to start that work now. Do not approve, do not ask it to pick something else, and do not start any implementation yourself.

In your final message, reproduce the skill's pick presentation verbatim — the repo and item it chose, its reasoning, the runner-ups it listed, and anything it said about repos or items it did not choose.
