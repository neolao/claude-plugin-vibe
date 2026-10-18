---
name: feature-returns-to-need-on-problem-space-finding
description: >-
  vibe:feature --auto on a brief that is silent about a business rule the
  project records in `.vibe/decisions/001` (missing readings are `null` and
  are skipped, never an error) must end with a median that skips `null`, and
  must have honoured the rule through the loop's own means: either the need
  framing cited the decision, or the internal review raised it as a need-space
  finding and the run went back to the need framing (`returns.need`, a
  `Round 2 —` task list). The project's CLAUDE.md convention ("validate input
  and throw") pulls the other way, which is what makes the rule easy to miss.
  Requires --allow-tools Bash,Write,Edit. Expensive (full --auto loop):
  validate alone with --runs 1 first.
tags: [feature, auto, loop, need-space]
runs: 1
max_turns: 140
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:feature` skill (Skill tool, `skill: "vibe:feature"`) with exactly this argument:

```
add a function that returns the median of a list of readings --auto
```

Work in the current directory. It already contains a small Node.js project (a source module, its test file, a passing `npm test` / `npm run lint` baseline, a `CHANGELOG.md`, a `.vibe/` context map with one decision record, and a git repository with one commit) — do not recreate any of this. Follow the skill's own instructions exactly, including its `--auto` mode gate table from `workflow.md`. There is no one to answer a question: every gate must resolve itself and the run must end with a machine-readable `AUTO-RESULT:` line.

In your final message, reproduce the skill's report verbatim, then add one line saying how many review rounds the run took.
