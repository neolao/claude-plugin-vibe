---
name: changelog-reuses-an-unreleased-heading-spelled-without-brackets
description: "/vibe:changelog, on a CHANGELOG.md whose pending section is headed `## Unreleased` (no brackets, like its `## 1.0.0 - 2026-06-01` section), must file the PDF export under that existing heading, keep its spelling, and add no second unreleased heading of any spelling. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, structure]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
