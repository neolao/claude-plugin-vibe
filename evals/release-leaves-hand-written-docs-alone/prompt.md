---
name: release-leaves-hand-written-docs-alone
description: >-
  vibe:release on a repo whose docs/ is hand-written (no vibe:docs
  banner) and whose README has no managed section must skip the docs
  step — vibe:docs never invoked, docs/ and README untouched — and still
  tag v1.3.0. Requires --allow-tools Bash,Write,Edit to run
  (Bash/Write/Edit are gated tools).
tags: [release, docs, precision]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with no arguments, so it reads `CHANGELOG.md` itself and suggests the version bump.

This is a non-interactive eval. If the skill asks you to confirm the suggested bump, confirm it and continue. If it asks you any other question, do not answer it: stop there and report the question as it was asked.

Do not push anything. `/vibe:release` never pushes, and neither should you.

Once the release is complete, run `git tag`, `git log --oneline -5` and `ls docs` with the Bash tool and include their raw output in your final message. Then report, in short plain sentences: the version released, what happened to the documentation, and confirmation that nothing was pushed.
