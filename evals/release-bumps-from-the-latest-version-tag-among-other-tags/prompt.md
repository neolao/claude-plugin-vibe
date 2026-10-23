---
name: release-bumps-from-the-latest-version-tag-among-other-tags
description: >-
  vibe:release with the argument `patch` must bump from the latest
  version-shaped tag (v1.2.3) when `vnext` and `deploy-2026-01-15` sort
  above it and no manifest can stand in: v1.2.4, not v0.0.1. Requires
  --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [release, versioning, tags]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `patch`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step — pre-release checks, finalizing the changelog, bumping the version, committing, and tagging — without waiting for further input. The project has no package manifest, no test, lint or build command: that is expected, not a problem to fix.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the release is complete, run `git tag` and `git log --oneline -5` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: the version released, the version you bumped from and how you chose it, and confirmation that nothing was pushed.
