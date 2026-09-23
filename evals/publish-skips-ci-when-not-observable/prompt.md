---
name: publish-skips-ci-when-not-observable
description: >-
  vibe:publish must skip its CI-verification step silently when the repo
  has no observable GitHub Actions workflow, with no blocker and no hang.
  Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated
  tools).
tags: [publish, ci]
runs: 3
max_turns: 20
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:publish` skill (Skill tool, `skill: "vibe:publish"`) with
no arguments. Work in the current directory exactly as it is — do not
recreate or reconfigure anything in it, and do not add a CI/deploy
workflow to it.

Then report, in short plain sentences, exactly what `vibe:publish` found
and reported.
