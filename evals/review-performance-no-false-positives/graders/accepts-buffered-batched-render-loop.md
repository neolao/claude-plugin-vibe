---
type: llm
focus: last_message
criteria: |
  `update_frame` in fixtures/render_loop.py clears and refills the
  module-level `_transform_buffer` and the per-texture lists of
  `_meshes_by_texture` at the start of every frame instead of allocating new
  ones, uploads the transforms in one call, and issues one `draw_batch` per
  texture rather than one draw call per entity. Nothing it owns grows from
  one frame to the next: the dict's keys are the current level's textures,
  reset by `load_level` once per level.

  PASS if no `high` or `medium` severity finding claims this loop allocates
  per frame, issues per-object draw calls, or accumulates meshes or keys
  across frames.
  FAIL if it is flagged as a Real-time issue (or equivalent) at high or
  medium severity.
weight: 1
---

Does not flag a buffer-reusing, texture-batched frame loop.
