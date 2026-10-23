---
name: publish-pushes-only-the-release-tag
description: >-
  vibe:publish must push the tag the release created, by name, and leave a
  never-published local tag where it is. Requires --allow-tools
  Bash,Write,Edit to run.
tags: [publish, e2e, tags]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:publish` skill (Skill tool, `skill: "vibe:publish"`) with no
arguments. Work in the current directory exactly as it is.

Once it finishes, run `git ls-remote --tags origin` and report its exact
output in your final message, together with `vibe:publish`'s own report.
