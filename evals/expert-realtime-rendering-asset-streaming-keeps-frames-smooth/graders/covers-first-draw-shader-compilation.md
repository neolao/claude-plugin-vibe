---
type: llm
focus: last_message
criteria: |
  The brief says the engine compiles the material's shader the first time the
  object is drawn. In WebGL the compile and link happen synchronously on the
  draw that first uses the program, so the first frame in which a streamed
  object is drawn with its real material pays the compilation: a visible
  hitch exactly when the object comes into view.

  PASS if REQUIREMENTS or RISKS flags the first-draw shader compilation as a
  stall in the frame where the object is first drawn and requires it warmed
  up off that moment: the material's shader variants compiled when the scene
  opens or when the asset is streamed in, a prewarm pass (an off-screen or
  one-pixel draw) before the object is shown, or the parallel-compile
  extension queried so the program is used only once it is ready.
  FAIL if the shader compilation at first draw is never raised, or is folded
  into a generic "preload assets" statement that does not name the shader
  compile as the cost.
weight: 2
---

Flags the first-draw shader compilation as a frame stall and requires it
warmed up before the object is shown.
