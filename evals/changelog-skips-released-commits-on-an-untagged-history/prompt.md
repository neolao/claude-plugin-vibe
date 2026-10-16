---
name: changelog-skips-released-commits-on-an-untagged-history
description: "/vibe:changelog, on a repository with no tag and a CHANGELOG.md whose [1.0.0] section already covers the first two features, must add only the two later commits under [Unreleased] (PDF export under Added, sort order under Fixed) and leave the released entries uncopied and untouched. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, no-tag]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
