---
name: next-task-resolves-a-bare-forced-pick-to-the-one-repo-holding-it
description: >-
  vibe:next-task given a bare `003` at a workspace root where only
  billing-web holds an item 003 must resolve it to billing-web and present
  billing-web 003 for confirmation, without asking which repo was meant.
  Stopped at the Step 6 confirmation. Requires `--allow-tools Bash` to run.
tags: [next-task, workspace, forced-pick, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

Invoke the `vibe:next-task` skill (Skill tool, `skill: "vibe:next-task"`) with `003` as `$ARGUMENTS` — the forced-pick form, with no repo named.

You are at the root of a workspace: a hub repo plus two active sibling repos, each with its own backlog. Everything is already set up — do not create, edit, or commit anything yourself.

When the skill presents its pick and asks for confirmation, **decline**: tell it plainly, in your own words, that you do not want to start that work now. Do not approve, do not ask it to pick something else, and do not start any implementation yourself. If it asks anything else, do not answer: reproduce the question in your final message instead.

In your final message, reproduce the skill's pick presentation verbatim — the repo and item it chose and its reasoning.
