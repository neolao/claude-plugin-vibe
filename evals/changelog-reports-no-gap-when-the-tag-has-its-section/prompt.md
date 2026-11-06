---
name: changelog-reports-no-gap-when-the-tag-has-its-section
description: "/vibe:changelog, on a repo tagged v1.0.0 and v1.1.0 where both have their section in CHANGELOG.md, must file the fix since v1.1.0 under [Unreleased] and report plainly, without warning about a missing section or a gap in the file. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, report, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed and what it noticed.
