---
type: llm
focus: last_message
criteria: |
  PASS if the final report states (or clearly implies) that sync ran in
  incremental mode — scoped to what changed since the last sync — rather
  than a full regeneration of `.vibe/`.
  FAIL if the report says it did a full regeneration, or does not indicate
  incremental scoping at all.
weight: 1
---

`.vibe/index.md` already existed in the fixture, so the skill's own rule
("full mode when `.vibe/index.md` is absent or `--full` is given;
incremental mode otherwise") means this run must be incremental.
