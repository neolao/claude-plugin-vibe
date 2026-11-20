---
name: release-reruns-lint-after-the-bump-and-formats-the-manifest
description: >-
  vibe:release must re-run lint after the version bump, fix the violation the bump exposed with the project's own formatter, re-check, then commit and tag. Requires --allow-tools Bash Write Edit to run (gated tools).
tags: [release, post-bump-check]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `patch`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step without waiting for further input. Follow the skill's own instructions for a failing check exactly as written.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the skill has finished (or otherwise concluded), run `git log --oneline -3`, `git tag` and `printf 'porcelain-lines|%s\n' "$(git status --porcelain --untracked-files=no | wc -l | tr -d ' ')"` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences, what the skill did and why.
