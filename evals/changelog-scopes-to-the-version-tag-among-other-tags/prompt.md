---
name: changelog-scopes-to-the-version-tag-among-other-tags
description: "/vibe:changelog, on a repo tagged v1.2.0 and, on a later commit, deploy-2026-10-30 and vnext, must take the commits since v1.2.0 (the latest version tag, not the latest tag): the PDF export under Added and the sort fix under Fixed, with the released [1.2.0] section untouched and no section created for the other tags. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, recall, tags]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
