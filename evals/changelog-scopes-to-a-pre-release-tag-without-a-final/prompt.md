---
name: changelog-scopes-to-a-pre-release-tag-without-a-final
description: "/vibe:changelog, on a repo tagged v1.2.0 then v1.3.0-rc.1 with no v1.3.0, must take the commits since v1.3.0-rc.1 — a pre-release is only skipped when its final version is also tagged — so only the PDF export lands under [Unreleased], not the CSV export already announced in [1.3.0-rc.1]. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, precision, tags]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
