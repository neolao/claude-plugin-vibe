---
name: changelog-leaves-accurate-unreleased-alone
description: "/vibe:changelog must recognise that [Unreleased] already covers every user-facing commit since v1.0.0, leave CHANGELOG.md untouched, and report that there was nothing to add — rather than duplicating entries or promoting noise. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
