---
name: changelog-classifies-by-prefix-over-keyword
description: "/vibe:changelog must file a feat: commit under Added even though its subject says auth, a fix: commit under Fixed even though its subject says remove, and classify a message that matches nothing (Monday changes) from its diff, which adds JSON output. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, classification]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
