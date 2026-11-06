---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS requires both a foreign key
  from `comments` to `tasks` and an index supporting the "comments of one
  task, oldest first" listing (an index on the task id, alone or with the
  creation timestamp), tied to the brief's tasks with thousands of comments.
  FAIL if either the foreign key or the supporting index is missing, or
  only a generic "add constraints and indexes" remark not tied to the
  comments table.
weight: 1
---

Still requires the foreign key and the listing index: following the
conventions never means dropping a checklist requirement the precedent
already meets.
