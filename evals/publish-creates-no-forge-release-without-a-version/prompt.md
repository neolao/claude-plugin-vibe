---
name: publish-creates-no-forge-release-without-a-version
description: >-
  vibe:publish must push the local commit, cut no release on an empty
  Unreleased section, and create no GitHub release — there is no version
  to announce. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit
  are gated tools).
tags: [publish, e2e, forge-release, precision]
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
