---
name: publish-fills-the-forge-release-notes-from-the-changelog
description: >-
  vibe:publish must create the GitHub release for the version it just
  pushed, with the changelog section as its notes, never --notes-from-tag.
  Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated
  tools).
tags: [publish, e2e, forge-release]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:publish` skill (Skill tool, `skill: "vibe:publish"`) with no
arguments. Work in the current directory exactly as it is — do not recreate
or reconfigure anything in it. The repo's `CLAUDE.md` says how commands are
run in this sandbox.

Then report, in short plain sentences, exactly what `vibe:publish` found
and reported.
