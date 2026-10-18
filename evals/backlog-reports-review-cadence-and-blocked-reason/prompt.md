---
name: backlog-reports-review-cadence-and-blocked-reason
description: >-
  vibe:backlog in list mode must surface 002's own blocked reason plus how to
  put it back in play, without editing anything. (The review-cadence hint this
  case used to check was removed with the `/vibe:review` command; the fixture's
  `.vibe/last-review.md` is now a legacy file the skill must ignore.)
tags: [backlog, list, blocked]
runs: 3
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:backlog` skill (Skill tool, `skill: "vibe:backlog"`) with an empty argument, to list the current backlog.

Report back the table it produced and every message that followed it, verbatim.
