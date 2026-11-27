---
type: llm
focus: last_message
criteria: |
  `Viewer.frame` in fixtures/viewer/frame.py compiles a material's shader
  with `gpu.compile_shader(...)` the first frame a mesh with that material
  is drawn, inside the loop over the scene's meshes, and caches it in
  `self._shaders` afterwards: the first frames of a scene each pay a
  compile and link on the GPU.

  PASS if the reported findings include a `Real-time` (or clearly
  equivalent category name) finding on this first-use `compile_shader`
  call in fixtures/viewer/frame.py, with a fix direction that compiles the
  scene's shaders at load time (or otherwise before the first frame).
  FAIL if no finding reports the shader compile inside the frame, or if it
  is reported only as `Blocking`.
weight: 1
---

Reports a shader compiled on first use inside the frame as a Real-time
stall.
