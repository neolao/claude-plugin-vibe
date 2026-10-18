---
name: review-orchestrates-active-agents-and-synthesizes
description: >
  vibe:review (internal brick) must fan out to exactly the always-active
  review-* agents (no CLAUDE.md table here, so it falls back to its own default
  list), skip every conditional agent a tiny script-only fixture doesn't warrant,
  and return their raw findings in the `## REVIEW …` contract — no fix, no
  commit, no severity change. Expensive: fans out to ~13 sub-agents per run;
  requires --allow-tools Bash (review-tests and review-dependencies execute).
tags: [review, orchestration]
runs: 1
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash]
---

Invoke the `vibe:review` skill (Skill tool, `skill: "vibe:review"`) with no arguments, so
it reviews the full codebase in the current workspace. Let it run to completion —
determining the active agents, running them, returning their findings — then report
back exactly what it returned.
