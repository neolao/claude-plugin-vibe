---
name: release-stops-when-nothing-is-left-to-release
description: >-
  vibe:release with the argument `patch` must stop without cutting a
  version when [Unreleased] is still empty after the changelog refresh:
  no tag, no bump, no dated section, and a report saying there is nothing
  to release. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit
  are gated tools).
tags: [release, changelog, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `patch`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it. Follow the skill's own instructions exactly as written — do not add a changelog entry yourself, and do not cut a release the skill decided not to cut.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the skill has stopped (or otherwise concluded), run `git tag` and `git log --oneline -5` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences, what the skill found and did.
