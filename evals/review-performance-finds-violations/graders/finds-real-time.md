---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Real-time` (or clearly equivalent
  category name) finding on `update_frame` in fixtures/render_loop.py, for
  either or both of: allocating a new `transform` dict and appending to a new
  `draw_calls` list on every entity every frame instead of reusing a buffer,
  or issuing one draw call per entity with no batching by texture/mesh.
  FAIL if no finding flags per-frame allocation or per-object draw calls in
  this loop.
weight: 1
---

Reports the per-frame allocation and/or unbatched per-entity draw calls in
`update_frame` as a `Real-time` finding.
