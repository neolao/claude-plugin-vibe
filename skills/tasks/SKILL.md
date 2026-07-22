---
name: tasks
description: Creates and tracks a vibe workflow's task list — uses the dedicated task system when available, falls back to a scratchpad checklist otherwise. Invoked internally by other vibe skills, never directly by users.
argument-hint: "<one task per line: '<subject> ← blockedBy \"<other subject>\"' or '<subject> ← no dependency'>"
user-invocable: false
---

# vibe:tasks — Task List Creation & Fallback

Invoked once per workflow run by another `vibe:*` skill, right after that skill's plan is approved. `$ARGUMENTS` is the task list to create: one task per line, subjects ≤ 30 chars, each with its `blockedBy` dependency or `no dependency`.

## Create the tasks

Create every task from `$ARGUMENTS` in order using `TaskCreate`, chaining dependencies with `addBlockedBy` exactly as given.

**If `TaskCreate` is not available in this environment:** say so explicitly (e.g. "The dedicated task system is not available in this environment — I will track progress via a checklist in my scratchpad directory instead") rather than silently failing or contradicting an earlier announcement. Write the task list from `$ARGUMENTS` as a Markdown checklist (`- [ ] <subject>`, in order) to `task-list.md` in your scratchpad directory instead.

## Standing instruction for the rest of this session

From here on, whenever the invoking skill's instructions say to mark a task `in_progress` or `completed`:
- If the dedicated task system was used above: call `TaskUpdate`.
- If the fallback was used: edit the matching line in `task-list.md` (check the box, or note it as started).

Do not re-invoke this skill for individual status updates — this instruction governs them for the remainder of the session.
