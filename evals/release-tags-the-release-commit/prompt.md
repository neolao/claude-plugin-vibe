---
name: release-tags-the-release-commit
description: >-
  vibe:release's tag must point at the release commit that carries the changelog cut and the manifest bump, and that commit must leave a clean tree. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [release, tags, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `patch`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step without waiting for further input.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the skill has finished (or otherwise concluded), run `git log -1 --format='target|%s' v1.2.4^{commit}`, `git show --stat --format='%s' HEAD` and `printf 'porcelain-lines|%s\n' "$(git status --porcelain | wc -l | tr -d ' ')"` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: what the skill did, which files you changed, and confirmation that nothing was pushed.
