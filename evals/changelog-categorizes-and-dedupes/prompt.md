---
name: changelog-categorizes-and-dedupes
description: "/vibe:changelog must classify commits since the last tag into the right Keep a Changelog categories, skip an entry that duplicates one already sitting in [Unreleased], discard merge/chore noise, and leave the released version section untouched. Requires --allow-tools Bash,Write,Edit to run (the skill reads git history and writes CHANGELOG.md)."
tags: [changelog, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
