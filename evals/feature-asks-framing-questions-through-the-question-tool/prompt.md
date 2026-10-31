---
name: feature-asks-framing-questions-through-the-question-tool
description: >-
  vibe:feature (interactive, not --auto) on "give customers a discount on
  large orders" must put its framing questions to the Product Owner through
  the AskUserQuestion tool, not as plain text at the end of a turn. The
  eval never offers that tool, so the case checks the run reaches for it
  (a call, or a ToolSearch loading it) before its text fallback. What counts as a large order and how
  much is taken off are product decisions no source in the fixture settles,
  so the need framing has to ask at least one of them. The run stops at the
  plan, before any code. Requires --allow-tools Bash Write Edit
  AskUserQuestion.
tags: [feature, clarify, questions]
runs: 3
max_turns: 60
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit, AskUserQuestion, TaskCreate, TaskUpdate]
---

Invoke the `vibe:feature` skill (Skill tool, `skill: "vibe:feature"`) with exactly this argument:

```
give customers a discount on large orders
```

Work in the current directory. It already contains a small Node.js project (a source module, its test file, a passing `npm test` / `npm run lint` baseline, a `CHANGELOG.md`, a `.vibe/` context map, and a git repository with one commit) — do not recreate any of this. Follow the skill's own instructions exactly.

You are also the Product Owner. Whenever the skill asks you something, answer right away with a clear, decisive choice of your own, without ending your turn, and let the skill go on.

When the skill presents its plan and asks for approval, stop there: do not approve it and do not write any code. In your final message, reproduce the plan as presented.
