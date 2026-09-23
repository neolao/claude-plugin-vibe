---
name: publish-verifies-ci-green
description: >-
  vibe:publish must detect a successful GitHub Actions run for the current
  commit and report it as green, with no false blocker. Requires
  --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [publish, ci]
runs: 3
max_turns: 20
timeout_seconds: 400
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:publish` skill (Skill tool, `skill: "vibe:publish"`) with
no arguments. Work in the current directory exactly as it is — do not
recreate or reconfigure anything in it.

Then report, in short plain sentences, exactly what `vibe:publish` found
and reported.
