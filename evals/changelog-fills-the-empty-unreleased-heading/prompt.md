---
name: changelog-fills-the-empty-unreleased-heading
description: "/vibe:changelog must reuse the existing empty [Unreleased] heading — not add a second one — and file the two commits under it in Keep a Changelog order (Added before Fixed), appending nothing below [1.0.0]. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, structure, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
