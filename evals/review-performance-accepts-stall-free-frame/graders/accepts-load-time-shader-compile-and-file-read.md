---
type: llm
focus: last_message
criteria: |
  `Viewer.load` in fixtures/viewer/frame.py reads `camera.json` and
  compiles every material's shader once, when the scene is opened and
  before its first frame; `Viewer.frame` only looks the compiled shaders
  up in `self._shaders`.

  PASS if no `high` or `medium` severity finding claims the shader compile
  or the camera file read runs inside a frame, stalls a frame or blocks the
  render loop. A `low` finding passes, and so does a report with no
  findings at all.
  FAIL if `compile_shader` in `load`, the `camera.json` read in `load`, or
  the shader lookup in `frame` is reported as Real-time or Blocking at high
  or medium severity.
weight: 1
---

Does not call load-time work a frame stall.
