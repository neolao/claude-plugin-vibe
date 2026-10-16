---
name: changelog-creates-the-file-from-the-whole-history-without-a-tag
description: "/vibe:changelog, on a repository with no tag and no CHANGELOG.md, must create the file with the Keep a Changelog header, one [Unreleased] section with the feature under Added and the fix under Fixed, no version section and no entry for the dependency bump. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, no-tag, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
