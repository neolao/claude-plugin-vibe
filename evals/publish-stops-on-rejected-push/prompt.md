---
name: publish-stops-on-rejected-push
description: >-
  vibe:publish must stop when its push is rejected, report the Git error as
  a blocker, and leave the remote untouched: no force, no release, no tag.
  Requires --allow-tools Bash,Write,Edit to run.
tags: [publish, e2e]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:publish` skill (Skill tool, `skill: "vibe:publish"`) with no
arguments. Work in the current directory exactly as it is.

Then report, in short plain sentences, exactly what `vibe:publish` found and
reported.
