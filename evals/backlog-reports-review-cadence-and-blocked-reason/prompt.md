---
name: backlog-reports-review-cadence-and-blocked-reason
description: >-
  vibe:backlog in list mode must report the recorded review date, count
  exactly the 6 feat/fix commits since its hash (not the 3 chore ones), and
  surface 002's own blocked reason plus how to put it back in play.
tags: [backlog, list, cadence]
runs: 3
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:backlog` skill (Skill tool, `skill: "vibe:backlog"`) with an empty argument, to list the current backlog.

Report back the table it produced and every message that followed it, verbatim.
