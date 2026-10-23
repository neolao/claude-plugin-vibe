---
name: release-cuts-the-changelog-without-links-when-there-is-no-remote
description: >-
  vibe:release with the argument `patch` on a repo with no remote must cut
  CHANGELOG.md without adding any link, and still commit and tag. Requires
  --allow-tools Bash,Write,Edit to run (Bash/Write/Edit are gated tools).
tags: [release, changelog, links, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with the argument `patch`.

This is a non-interactive eval: if the skill asks you to confirm anything, confirm it and continue through every remaining step — pre-release checks, finalizing the changelog, bumping the version, committing, and tagging — without waiting for further input. The repo has no remote: that is expected, do not add one.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the release is complete, run `git tag` and `tail -3 CHANGELOG.md` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: the version released, which files you changed, and confirmation that nothing was pushed.
