---
name: auto-ships-one-item-and-journals-state
description: >
  vibe:auto ships exactly one eligible backlog item through the underlying
  feature/fix workflow via a dedicated general-purpose sub-agent, journals
  the run in .vibe/auto-state.md, moves the closed item to
  .vibe/backlog/done/, and reports why it stopped. Deliberately runs 1
  (not the usual 3) given the cost of a full autonomous feature cycle.
tags: [auto, e2e]
runs: 1
max_turns: 80
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit]
---

Invoke the `vibe:auto` skill (Skill tool, `skill: "vibe:auto"`) with argument `1`.

Let it run to completion, including the sub-agent it dispatches to implement
the backlog item. Report its final status lines and closing report back
verbatim.
