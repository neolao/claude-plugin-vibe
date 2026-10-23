---
name: publish-pushes-no-tag-without-a-release
description: >-
  vibe:publish must push the local commit, cut no release on an empty
  Unreleased section, and push no tag — the never-published local tag
  stays local. Requires --allow-tools Bash,Write,Edit to run.
tags: [publish, e2e, tags, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:publish` skill (Skill tool, `skill: "vibe:publish"`) with no
arguments. Work in the current directory exactly as it is.

Once it finishes, run `git ls-remote --tags origin` and report its exact
output in your final message, together with `vibe:publish`'s own report.
