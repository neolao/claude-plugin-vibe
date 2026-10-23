---
name: release-writes-https-links-from-an-ssh-remote
description: >-
  vibe:release with the argument `patch` on a repo with an SSH origin must
  write https compare links at the bottom of CHANGELOG.md, never the SSH
  URL. Requires --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are
  gated tools).
tags: [release, changelog, links]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `patch`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step — pre-release checks, finalizing the changelog, bumping the version, committing, and tagging — without waiting for further input.

Do not push anything. `/vibe:release` never pushes, and neither should you. The sandbox has no network: the remote is never contacted, only its URL is read.

Once the release is complete, run `git tag` and `tail -3 CHANGELOG.md` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: the version released, which files you changed, and confirmation that nothing was pushed.
