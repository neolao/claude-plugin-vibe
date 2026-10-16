---
name: backlog-lists-missing-dependency-as-missing
description: >-
  vibe:backlog in list mode must mark 002's dependency on 009 as missing
  (no such item exists), keep 001 as an ordinary unmet dependency, explain
  that 002 stays ineligible for /vibe:auto until 009 is removed from its
  depends_on, and write nothing to disk.
tags: [backlog, list, read-only, dependencies]
runs: 3
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit]
---

Invoke the `vibe:backlog` skill (Skill tool, `skill: "vibe:backlog"`) with an empty argument, to list the current backlog.

Report back the table it produced and every message that followed it, verbatim.
