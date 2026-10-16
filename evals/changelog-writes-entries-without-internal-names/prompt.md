---
name: changelog-writes-entries-without-internal-names
description: "/vibe:changelog must turn developer-worded commits (function, class, file and parameter names in the subject) into user-facing entries under [Unreleased] that name none of those identifiers, not even in backticks, while classifying them under Added and Fixed. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, wording]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
