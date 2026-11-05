---
type: llm
focus: last_message
criteria: |
  The plan draws each of up to 1,500 labels with its own draw call and its
  own texture, interleaved with the objects: the draw-call count and the
  texture switches grow with the scene and eat the frame budget.

  PASS if REQUIREMENTS or RISKS requires the labels to be submitted in a few
  draws instead of one per label: batched or instanced quads, a single
  texture atlas (or a glyph atlas with text built into one buffer) so the
  labels share a texture, or labels drawn in one pass after the objects.
  FAIL if the reply never questions the one-draw-per-label plan, or covers
  it only as a generic "reduce draw calls" with no link to the labels.
weight: 2
---

Requires the labels to share draw submission (batching, instancing or an
atlas) rather than one draw call and one texture per label.
