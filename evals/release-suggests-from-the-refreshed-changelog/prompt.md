---
name: release-suggests-from-the-refreshed-changelog
description: >-
  vibe:release with no argument must bring the changelog up to date before
  suggesting the bump: a feat: commit absent from [Unreleased] makes it
  minor (v1.3.0), not the patch the stale section suggests. Requires
  --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [release, changelog, versioning]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with no arguments, so it reads the project itself and suggests the version bump.

This is a non-interactive eval: if the skill asks you to confirm the suggested bump (or any other step), confirm it and continue through every remaining step — pre-release checks, finalizing the changelog, bumping the version, committing, and tagging — without waiting for further input.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the release is complete, run `git tag` and `git log --oneline -5` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: the version released, the bump you suggested and why, and confirmation that nothing was pushed.
