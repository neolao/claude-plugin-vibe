---
name: changelog-inserts-the-heading-when-unreleased-is-only-an-entry
description: "/vibe:changelog, on a CHANGELOG.md with no [Unreleased] heading whose [1.0.0] section holds the entry \"List unreleased drafts in the report overview\", must still insert one `## [Unreleased]` above `## [1.0.0]`, file the PDF export under it, and leave the released section untouched. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, structure, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
