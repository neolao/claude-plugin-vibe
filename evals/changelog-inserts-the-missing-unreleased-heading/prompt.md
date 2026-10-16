---
name: changelog-inserts-the-missing-unreleased-heading
description: "/vibe:changelog must insert the missing [Unreleased] heading above the first version section — once — and file the two commits under it in Keep a Changelog order (Added before Fixed, although the fix came first), appending nothing below [1.0.0]. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, structure]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
