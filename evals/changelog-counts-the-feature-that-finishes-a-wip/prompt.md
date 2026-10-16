---
name: changelog-counts-the-feature-that-finishes-a-wip
description: "/vibe:changelog must record the PDF export once under Added when a wip: commit started it and a later feat: commit finished it — neither zero entries (wip rule applied to the feature) nor two (one per commit). Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, noise, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
