---
name: expert-data-counter-column-has-one-writer
description: >-
  Recall of the derived-value bullet of expert-data: the task list shows
  the number of live comments of each task, computed today with a
  per-task count that makes the list slow, and a `comment_count` column
  is to be added on a large tasks table while comments are posted and
  archived from three different clients. The expert must require one
  writer that keeps the count consistent with the comments (the
  comment's own transaction through a trigger or a shared write path, or
  a scheduled rebuild) and a way to compute the existing tasks' counts
  and recompute a drifted one — instead of a plain column each client
  updates as it likes.
tags: [expert-data, recall, derived-data]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-data` sub-agent (Agent tool, `subagent_type: "vibe:expert-data"`) with this brief plus the consultation request below.

Brief:

```
The task list shows, next to each task, how many comments it has (archived
comments don't count). Today the list runs one `COUNT(*)` over `comments`
per task and the page has become slow: `tasks` has three million rows and
`comments` forty million. We want a `comment_count` column on `tasks` that
the list reads directly. Comments are posted and archived from the web app,
from the mobile app through the public API, and from the support team's
admin console, which has its own code path. Nothing else in the schema
changes.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
