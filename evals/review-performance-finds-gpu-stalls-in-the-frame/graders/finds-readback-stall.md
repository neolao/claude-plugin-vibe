---
type: llm
focus: last_message
criteria: |
  `object_under_cursor` in fixtures/viewer/picking.py calls
  `gpu.read_pixels(...)`, which (fixtures/viewer/gpu.py) copies a region
  of the framebuffer back to the CPU once the GPU has finished every
  command issued so far; `Viewer.frame` in fixtures/viewer/frame.py calls
  it every frame, right after issuing the frame's draw calls, so each frame
  waits for the GPU to drain before it can end.

  PASS if the reported findings include a `Real-time` (or clearly
  equivalent category name) finding on `read_pixels` or
  `object_under_cursor`, anchored on fixtures/viewer/picking.py or
  fixtures/viewer/frame.py, that names it as a synchronous readback or GPU
  stall inside the frame. The fix direction should make it asynchronous
  (a request whose result is read a frame later) or move it off the frame.
  FAIL if no finding reports this readback, or if it is reported only as
  `Blocking` (it is a GPU stall, not I/O or parsing).
weight: 2
---

Reports a synchronous readback inside the frame as a Real-time stall.
