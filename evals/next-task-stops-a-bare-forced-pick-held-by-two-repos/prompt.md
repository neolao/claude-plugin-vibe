---
name: next-task-stops-a-bare-forced-pick-held-by-two-repos
description: >-
  vibe:next-task given a bare `001` at a workspace root where billing-api
  and billing-web both hold an item 001 must stop and name both repos,
  without presenting either item as the pick and without handing anything
  off. Requires `--allow-tools Bash` to run.
tags: [next-task, workspace, forced-pick]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

Invoke the `vibe:next-task` skill (Skill tool, `skill: "vibe:next-task"`) with `001` as `$ARGUMENTS` — the forced-pick form, with no repo named.

You are at the root of a workspace: a hub repo plus two active sibling repos, each with its own backlog. Everything is already set up — do not create, edit, or commit anything yourself.

If the skill presents a pick and asks for confirmation, **decline**: tell it plainly, in your own words, that you do not want to start that work now. Do not approve, do not ask it to pick something else, and do not start any implementation yourself.

In your final message, reproduce the skill's final message verbatim — what it said about the number, the repos, and any pick it presented.
