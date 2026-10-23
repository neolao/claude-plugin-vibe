---
name: release-bumps-from-the-manifest-when-nothing-is-tagged
description: >-
  vibe:release with the argument `minor` on a repo with no tag must bump
  from the manifest's version (0.4.0): v0.5.0, not v0.1.0 and not a
  refusal. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit
  are gated tools).
tags: [release, versioning, tags, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `minor`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step — pre-release checks, finalizing the changelog, bumping the version, committing, and tagging — without waiting for further input. The repo has no tag yet: that is expected, not a problem to fix.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the release is complete, run `git tag` and `git log --oneline -5` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: the version released, the version you bumped from and where it came from, and confirmation that nothing was pushed.
