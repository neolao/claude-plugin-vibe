---
name: changelog-records-the-revert-of-a-released-feature
description: "/vibe:changelog must record the revert of a feature released in 1.1.0 as a Removed entry under [Unreleased], worded as the export the user loses rather than as a Revert, and leave both released sections byte-for-byte untouched. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, revert, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
