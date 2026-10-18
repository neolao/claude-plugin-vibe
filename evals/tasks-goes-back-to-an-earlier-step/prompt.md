---
name: tasks-goes-back-to-an-earlier-step
description: vibe:tasks (internal) must apply its "Going back" section when a workflow returns to an earlier step — the current task goes completed, every pending task is dropped (deleted, announced with ✗ … — stale), no completed task is touched, and the new round's tasks carry the `Round 2 — ` prefix. Runs in Docker (Bash granted for the script) so the fallback path is the one measured; requires --allow-tools Bash Write Edit.
tags: [tasks, going-back]
runs: 3
max_turns: 25
timeout_seconds: 300
allowed_tools: [Read, Skill, Bash, Write, Edit]
---

Invoke the `vibe:tasks` skill (Skill tool, `skill: "vibe:tasks"`) with this argument, verbatim:

```
Plan ← no dependency
Implement ← blockedBy "Plan"
Review ← blockedBy "Implement"
Commit ← blockedBy "Review"
```

Then follow the skill's own "Standing instruction for the rest of this session": mark "Plan" `in_progress` then `completed`, "Implement" `in_progress` then `completed`, and "Review" `in_progress`.

At that point the review finds that the plan missed a requirement: the workflow goes back to the planning step. Apply the skill's "Going back" section, exactly as written, for a second round made of the same four steps (Plan, Implement, Review, Commit).

Stop once the second round's four tasks exist and the first of them is `in_progress`. Report back every status line you printed, in order, and the final task list as the skill shows it.
