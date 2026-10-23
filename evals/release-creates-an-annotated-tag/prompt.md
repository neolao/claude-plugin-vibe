---
name: release-creates-an-annotated-tag
description: >-
  vibe:release must create an annotated tag whose subject is the version and whose body holds the cut section's entries, not a lightweight tag. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [release, tags]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `patch`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step without waiting for further input.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the skill has finished (or otherwise concluded), run `git for-each-ref refs/tags/v1.2.4 --format='%(objecttype)|%(contents:subject)'` and `git tag -n20 v1.2.4` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: what the skill did, which files you changed, and confirmation that nothing was pushed.
