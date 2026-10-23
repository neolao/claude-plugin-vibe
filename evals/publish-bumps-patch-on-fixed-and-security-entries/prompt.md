---
name: publish-bumps-patch-on-fixed-and-security-entries
description: >-
  vibe:publish must decide a patch bump from an Unreleased section holding
  only Fixed and Security entries, pass it explicitly to vibe:release, and
  push v1.0.1 to the local bare origin. Requires --allow-tools
  Bash,Write,Edit to run.
tags: [publish, e2e, versioning, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:publish` skill (Skill tool, `skill: "vibe:publish"`) with no
arguments. Work in the current directory exactly as it is.

Once it finishes, run `git ls-remote --tags origin` and report its exact
output in your final message, together with `vibe:publish`'s own report.
