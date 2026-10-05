---
name: release-minor-bumps-every-manifest-from-numeric-latest-tag
description: vibe:release with the argument `minor` must bump from the numerically latest tag (v1.10.0, not v1.9.0), update every manifest (package.json and pyproject.toml) to 1.11.0, cut CHANGELOG.md with correct compare links, commit and tag — without pushing. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [release, versioning, manifests]
runs: 3
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `minor`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step — pre-release checks, finalizing the changelog, bumping the version, committing, and tagging — without waiting for further input.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the release is complete, run `git tag` and `git log --oneline -5` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: the version released, which files you changed, and confirmation that nothing was pushed.
