---
name: publish-moves-on-when-no-run-is-triggered
description: >-
  vibe:publish must stop waiting for a workflow run that never appears
  after its two-minute bound, report CI as not observable with no blocker,
  and not hang until its ten-minute poll limit. Requires --allow-tools
  Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [publish, ci]
runs: 3
max_turns: 25
timeout_seconds: 420
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:publish` skill (Skill tool, `skill: "vibe:publish"`) with
no arguments. Work in the current directory exactly as it is — do not
recreate or reconfigure anything in it. The repo's `CLAUDE.md` says how
commands are run in this sandbox.

Then report, in short plain sentences, exactly what `vibe:publish` found
and reported.
