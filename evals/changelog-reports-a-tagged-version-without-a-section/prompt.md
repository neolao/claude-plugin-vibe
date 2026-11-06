---
name: changelog-reports-a-tagged-version-without-a-section
description: "/vibe:changelog, on a repo tagged v1.0.0 (with its section) and v1.1.0 (tagged by hand, no section in CHANGELOG.md), must file only the fix since v1.1.0 under [Unreleased], create no [1.1.0] section, and say in its report that v1.1.0 has no section so its CSV export is written up nowhere. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, report, tags]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed and what it noticed.
