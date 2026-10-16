---
name: changelog-drops-wip-and-invisible-commits
description: "/vibe:changelog must discard a wip: commit with no follow-up (no Added entry for the PDF export it started), a refactor and a test commit with no user-visible effect, and still record the one real fix under Fixed. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, noise]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
