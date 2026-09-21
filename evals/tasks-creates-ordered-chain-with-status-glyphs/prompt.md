---
name: tasks-creates-ordered-chain-with-status-glyphs
description: vibe:tasks (internal, user-invocable false but directly callable for eval purposes) must create a 3-task chain with blockedBy dependencies — via TaskCreate, or a task-list.md checklist if TaskCreate is unavailable — then print the exact ● / ✓ status-glyph lines on transition; requires --allow-tools Write for the fallback path
tags: [tasks, status-glyphs]
runs: 3
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Skill, TaskCreate, TaskUpdate, Write]
---

Invoke the `vibe:tasks` skill (Skill tool, `skill: "vibe:tasks"`) with this argument, verbatim:

```
Write tests ← no dependency
Implement ← blockedBy "Write tests"
Commit ← blockedBy "Implement"
```

Once the task list exists, follow the skill's own "Standing instruction for the rest of this session": mark "Write tests" `in_progress`, then mark it `completed`. For each transition, print the exact compact status line the skill specifies.

Report back every status line you printed, in order, and how the task list was tracked (dedicated task system or scratchpad checklist).
