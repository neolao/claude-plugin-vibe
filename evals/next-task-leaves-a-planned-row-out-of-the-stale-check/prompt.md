---
name: next-task-leaves-a-planned-row-out-of-the-stale-check
description: >-
  vibe:next-task in workspace scope must take the registry as it is — a
  planned row has no directory by definition — and pick billing-api 001, the
  only unblocked candidate of the only active repo, without offering the
  archived legacy-batch repo's item, which a sibling scan would have brought
  in. Stopped at the Step 6 confirmation. Requires `--allow-tools Bash` to
  run.
tags: [next-task, workspace, registry]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash]
---

Invoke the `vibe:next-task` skill (Skill tool, `skill: "vibe:next-task"`) with an empty argument — the normal mode, where it picks a candidate itself and asks you to confirm before doing anything.

You are at the root of a workspace: a hub repo plus sibling repos, each with its own backlog. Everything is already set up — do not create, edit, or commit anything yourself.

When the skill presents its pick and asks for confirmation, **decline**: tell it plainly, in your own words, that you do not want to start that work now. Do not approve, do not ask it to pick something else, and do not start any implementation yourself.

In your final message, reproduce the skill's pick presentation verbatim — the repo and item it chose, its reasoning, the runner-ups it listed, and anything it said about the registry or about items it did not choose.
