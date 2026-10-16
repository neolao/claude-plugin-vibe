---
name: changelog-keeps-user-typed-names
description: "/vibe:changelog must keep the user-typed names in its entries — the new `--json` flag under Added and the deprecated `/v1/reports` endpoint under Deprecated — while still leaving the released section untouched. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, wording, precision]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
