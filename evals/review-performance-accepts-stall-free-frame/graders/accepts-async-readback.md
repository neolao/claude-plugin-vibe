---
type: llm
focus: last_message
criteria: |
  `Picker` in fixtures/viewer/picking.py requests the readback with
  `gpu.request_read_pixels(...)` at the end of a frame (nothing waits, per
  fixtures/viewer/gpu.py) and collects it at the start of the next frame
  with `gpu.read_if_ready(...)`, which returns None while the GPU is still
  on it: no frame waits for the GPU.

  PASS if no `high` or `medium` severity finding claims the picking
  readback stalls, blocks or waits for the GPU inside the frame. A `low`
  finding passes, and so does a report with no findings at all.
  FAIL if `request_read_pixels`, `read_if_ready`, `Picker.collect` or
  `Picker.request` is reported as a Real-time stall or Blocking at high or
  medium severity.
weight: 2
---

Does not call an asynchronous readback, collected a frame later, a stall.
