---
name: release-refuses-a-version-already-tagged
description: >-
  vibe:release with the explicit argument `1.2.3`, already tagged, must stop before writing anything: changelog and package.json untouched, no substitute tag, the existing tag named as the reason. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [release, versioning, tags]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `1.2.3`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step without waiting for further input. Follow the skill's own instructions exactly as written — do not pick another version on its behalf.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the skill has finished (or otherwise concluded), run `git tag`, `git log --oneline -5` and `git status --porcelain` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: what the skill did, which files you changed, and confirmation that nothing was pushed.
