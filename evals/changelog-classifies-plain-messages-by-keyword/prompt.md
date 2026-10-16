---
name: changelog-classifies-plain-messages-by-keyword
description: "/vibe:changelog must classify plain, prefix-less messages by their keywords — Add → Added, Remove → Removed, Patch → Fixed — and drop a README typo fix as noise. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, classification, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
