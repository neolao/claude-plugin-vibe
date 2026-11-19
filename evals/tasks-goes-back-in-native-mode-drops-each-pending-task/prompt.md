---
name: tasks-goes-back-in-native-mode-drops-each-pending-task
description: >-
  vibe:tasks (internal) must apply its "Going back" section in native mode,
  where there is no drop-pending command. With two pending tasks at the time
  of the return, the current task goes completed, each pending task gets its
  own deleted transition through TaskUpdate, lowest id first, each announced
  with its own stale line, no completed task is touched, and the new round's
  tasks carry the Round 2 prefix in their status line. Runs on the host (no
  Bash), so the native task system is the path measured.
tags: [tasks, going-back, native]
runs: 3
max_turns: 40
timeout_seconds: 300
allowed_tools: [Read, Skill, TaskCreate, TaskUpdate, TaskList, TaskGet]
---

Invoke the `vibe:tasks` skill (Skill tool, `skill: "vibe:tasks"`) with this argument, verbatim:

```
Plan ← no dependency
Implement ← blockedBy "Plan"
Review ← blockedBy "Implement"
Document ← blockedBy "Review"
Commit ← blockedBy "Document"
```

Then follow the skill's own "Standing instruction for the rest of this session": mark "Plan" `in_progress` then `completed`, "Implement" `in_progress` then `completed`, and "Review" `in_progress`.

At that point the review finds that the plan missed a requirement: the workflow goes back to the planning step. Apply the skill's "Going back" section, exactly as written, for a second round made of the same five steps (Plan, Implement, Review, Document, Commit).

Stop once the second round's five tasks exist and the first of them is `in_progress`. Report back every status line you printed, in order, and the final task list as the skill shows it.
