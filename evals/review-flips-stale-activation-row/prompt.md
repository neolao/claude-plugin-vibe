---
name: review-flips-stale-activation-row
description: >
  /vibe:review must flip the activation row whose stated project fact is no
  longer true (no HTTP surface, while Flask routes exist), leave the two rows
  recording a deliberate user choice untouched, report the flip, and commit the
  corrected CLAUDE.md. Needs --allow-tools Bash Write Edit to run.
tags: [review, activation-table]
runs: 1
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit]
---

Invoke the `vibe:review` skill (Skill tool, `skill: "vibe:review"`) with no arguments,
so it reviews the full codebase in the current workspace. Let it run to completion —
determining the active agents, running them, applying fixes, syncing, and committing —
then report back what it did, including any activation-table row it changed.
