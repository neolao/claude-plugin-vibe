---
name: release-restores-the-tree-when-the-re-check-still-fails
description: >-
  vibe:release must stop without committing or tagging when the re-check after the version bump fails and the project has no formatter, and leave the tree as it was. Requires --allow-tools Bash Write Edit to run (gated tools).
tags: [release, post-bump-check, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `patch`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step without waiting for further input. Follow the skill's own instructions for a failing check exactly as written.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the skill has finished (or otherwise concluded), run `git log --oneline -3`, `git tag` and `printf 'porcelain-lines|%s\n' "$(git status --porcelain --untracked-files=no | wc -l | tr -d ' ')"` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences, what the skill did and why.
