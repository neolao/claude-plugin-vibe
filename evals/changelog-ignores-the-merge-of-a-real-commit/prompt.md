---
name: changelog-ignores-the-merge-of-a-real-commit
description: "/vibe:changelog must record the PDF export exactly once under Added when a pull request's branch holds a real feat: commit and the merge message says the same thing — the merge is noise, not a second entry. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, merge, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
