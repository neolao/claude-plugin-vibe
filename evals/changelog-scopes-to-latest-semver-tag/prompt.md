---
name: changelog-scopes-to-latest-semver-tag
description: "/vibe:changelog must take the commits since the highest version tag (v1.10.0, not the lexically last v1.9.0), classify scoped conventional commits into Added, Changed, Deprecated, skip a fix that [Unreleased] already describes in other words, discard a chore and a merge, and leave both released sections untouched. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, recall, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
