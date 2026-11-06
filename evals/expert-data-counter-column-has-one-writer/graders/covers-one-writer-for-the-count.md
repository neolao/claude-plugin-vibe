---
type: llm
focus: last_message
criteria: |
  `tasks.comment_count` is a copy of what `COUNT(*)` over the task's
  live comments would return, and comments are posted and archived from
  three places: the web app, the mobile app through the API, and the
  support team's admin console. The expert's checklist says a derived
  value has one writer that keeps it consistent — the same transaction as
  its source, a trigger, or a scheduled rebuild.

  PASS if REQUIREMENTS names the one mechanism that keeps
  `comment_count` consistent with the comments — the count changed in the
  same database transaction as the comment insert and the archive
  (through a trigger or one shared write path that the three clients all
  go through), or a scheduled rebuild with the lag it allows — and ties
  it to the three places that write comments so none of them can update
  comments without updating the count.
  FAIL if the reply prescribes the column with no mechanism keeping it
  equal to the comments, lets each of the three clients update the count
  on its own, or updates the count outside the transaction that inserts
  or archives the comment with no word on the drift that allows.
weight: 2
---

Names the one writer — the comment's own transaction (trigger or shared
write path) or a scheduled rebuild — that keeps the count consistent for
the three places that write comments.
