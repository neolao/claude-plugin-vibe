---
name: review-orchestrates-active-agents-and-synthesizes
description: >
  /vibe:review must fan out to exactly the always-active review-* agents (no CLAUDE.md
  table here, so it falls back to its own default list), skip every conditional agent
  a tiny script-only fixture doesn't warrant, synthesize their findings instead of
  dumping raw agent output, and record + commit the run. Expensive: fans out to ~9
  sub-agents per run (the always-active set) plus fix/commit steps; requires
  --allow-tools Bash Write Edit to run since the skill applies fixes and commits.
tags: [review, orchestration]
runs: 1
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit]
---

Invoke the `vibe:review` skill (Skill tool, `skill: "vibe:review"`) with no arguments, so
it reviews the full codebase in the current workspace. Let it run to completion —
determining the active agents, running them, deduplicating and prioritizing findings,
applying fixes, syncing, and committing — then report back what it did.
