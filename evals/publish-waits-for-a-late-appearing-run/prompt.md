---
name: publish-waits-for-a-late-appearing-run
description: >-
  vibe:publish must keep looking for the workflow run during its bounded
  wait, find the run once it is listed, and report it green — never
  "not observable" from the first empty listing. Requires --allow-tools
  Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [publish, ci, precision]
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
