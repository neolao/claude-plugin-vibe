---
name: next-task-scores-candidates-across-workspace
description: >-
  vibe:next-task in workspace scope must detect the hub, collect candidates
  from both active repos, keep orders-api 001 blocked because "publishes
  v0.3.0" needs a pushed tag and not merely a done item, keep orders-api 002
  blocked on orders-sdk#001, never treat the hub's own item as candidate work,
  and pick orders-sdk 001 because orders-api 002 waits on it. Stopped at the
  Step 6 confirmation, so no implementation runs. Requires `--allow-tools Bash`
  to run.
tags: [next-task, workspace, scoring]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

Invoke the `vibe:next-task` skill (Skill tool, `skill: "vibe:next-task"`) with an empty argument — the normal mode, where it picks a candidate itself and asks you to confirm before doing anything.

You are at the root of a workspace: a hub repo plus two active sibling repos, each with its own backlog. Everything is already set up — do not create, edit, or commit anything yourself.

When the skill presents its pick and asks for confirmation, **decline**: tell it plainly, in your own words, that you do not want to start that work now. Do not approve, do not ask it to pick something else, and do not start any implementation yourself.

In your final message, reproduce the skill's pick presentation verbatim — the repo and item it chose, its reasoning, the runner-ups it listed, and anything it said about items it did not choose.
