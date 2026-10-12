---
name: review-flips-active-rows-off-and-scopes-to-path
description: >
  /vibe:review must switch off the two active rows whose stated project fact is
  false, keep the explicit opt-in row, run only the two remaining agents, stay
  within the src/ argument, report the flips and commit. Needs
  --allow-tools Bash Write Edit to run.
tags: [review, activation-table, scope]
runs: 1
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit]
---

Invoke the `vibe:review` skill (Skill tool, `skill: "vibe:review"`) with the argument `src/`,
so it reviews only that path. Let it run to completion — determining the active agents,
running them, applying fixes, syncing, and committing — then report back what it did,
including any activation-table row it changed.
