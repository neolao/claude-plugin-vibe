---
name: release-leaves-a-settings-format-version-alone
description: >-
  vibe:release with the argument `patch` must bump package.json to 1.2.4 and leave the "version": 2 of config/settings.json — a settings format version — untouched. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [release, versioning, manifests, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `patch`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step without waiting for further input.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the skill has finished (or otherwise concluded), run `git tag` and `git show --stat HEAD` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: what the skill did, which files you changed, and confirmation that nothing was pushed.
