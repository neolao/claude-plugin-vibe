---
type: llm
focus: last_message
criteria: |
  `update_frame` in fixtures/render_loop.py clears and refills the
  module-level `_transform_buffer` instead of allocating a new list, uploads
  it in one call, and issues one `draw_batch` per texture rather than one
  draw call per entity.

  PASS if no `high` or `medium` severity finding claims this loop allocates
  per frame or issues per-object draw calls.
  FAIL if it is flagged as a Real-time issue (or equivalent) at high or
  medium severity.
weight: 1
---

Does not flag a buffer-reusing, texture-batched frame loop.
