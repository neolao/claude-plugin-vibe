---
name: backlog-lists-with-dependency-status
description: vibe:backlog in list mode must show 002 as blocked-by 001 (⚠ marker), surface 003's own blocked reason, report the done count, note no review has run yet, and write nothing to disk — requires --allow-tools Write Edit to make the read-only assertion meaningful (list mode needs no Bash when no `.vibe/last-review.md` exists)
tags: [backlog, list, read-only]
runs: 3
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit]
---

Invoke the `vibe:backlog` skill (Skill tool, `skill: "vibe:backlog"`) with an empty argument, to list the current backlog.

Report back the table it produced and every message that followed it, verbatim.
