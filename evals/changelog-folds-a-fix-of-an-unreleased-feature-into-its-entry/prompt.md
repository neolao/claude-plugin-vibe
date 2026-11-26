---
name: changelog-folds-a-fix-of-an-unreleased-feature-into-its-entry
description: >-
  /vibe:changelog, after a PDF export, a fix for a crash in that unreleased
  PDF export, and a fix for the released pagination, must list the PDF export
  under Added and only the pagination fix under Fixed. Requires
  --allow-tools Bash,Write,Edit to run.
tags: [changelog, classification]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
