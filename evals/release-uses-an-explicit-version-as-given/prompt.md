---
name: release-uses-an-explicit-version-as-given
description: >-
  vibe:release with the explicit argument `2.0.0` must release exactly that version — tag v2.0.0, section [2.0.0], package.json 2.0.0 — not the patch its Fixed-only changelog would suggest. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [release, versioning, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `2.0.0`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step without waiting for further input.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the skill has finished (or otherwise concluded), run `git tag` and `git log --oneline -5` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: what the skill did, which files you changed, and confirmation that nothing was pushed.
