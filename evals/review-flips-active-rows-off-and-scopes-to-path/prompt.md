---
name: review-flips-active-rows-off-and-scopes-to-path
description: >
  /vibe:review must switch off the two active rows whose stated project fact is
  false, keep the explicit opt-in row, run only the two remaining agents, stay
  within the src/ argument, and list the flips in its output.
  Needs --allow-tools Bash Edit to run (Edit for the CLAUDE.md table).
tags: [review, activation-table, scope]
runs: 1
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Edit]
---

Invoke the `vibe:review` skill (Skill tool, `skill: "vibe:review"`) with the argument `src/`,
so it reviews only that path. Let it run to completion — determining the active agents,
running them, returning their findings — then report back exactly what it returned,
including the `## REVIEW flipped rows` section.
