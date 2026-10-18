---
name: review-flips-stale-activation-row
description: >
  /vibe:review must flip the activation row whose stated project fact is no
  longer true (no HTTP surface, while Flask routes exist), leave the two rows
  recording a deliberate user choice untouched, and list the flip in its output;
  the caller commits CLAUDE.md. Needs --allow-tools Bash Edit to run.
tags: [review, activation-table]
runs: 1
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Edit]
---

Invoke the `vibe:review` skill (Skill tool, `skill: "vibe:review"`) with no arguments,
so it reviews the full codebase in the current workspace. Let it run to completion —
determining the active agents, running them, returning their findings — then report back
exactly what it returned, including the `## REVIEW flipped rows` section.
