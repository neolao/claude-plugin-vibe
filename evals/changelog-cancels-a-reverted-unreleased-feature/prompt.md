---
name: changelog-cancels-a-reverted-unreleased-feature
description: "/vibe:changelog must cancel a feat: commit against the Revert commit that undid it in the same range — removing the PDF entry the feature had written under [Unreleased], opening no Removed section — while still recording the unrelated fix under Fixed. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, revert]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
