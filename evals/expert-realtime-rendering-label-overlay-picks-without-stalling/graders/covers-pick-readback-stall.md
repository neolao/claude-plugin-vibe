---
type: llm
focus: last_message
criteria: |
  The plan renders the scene again and reads the pixel under the cursor back
  to the CPU on every mouse move: a synchronous GPU-to-CPU readback in the
  middle of the frame blocks until the GPU has finished all pending work.

  PASS if REQUIREMENTS or RISKS names this readback as a pipeline stall and
  requires a way around it: an asynchronous readback (pixel buffer object
  with a fence or a one-frame delay), reading back only a one-pixel region,
  limiting the picking pass to at most once per frame instead of once per
  mouse event, or keeping the CPU ray test and using the picking pass only
  where it is needed.
  FAIL if the reply never raises the readback as a stall, or only says
  "optimize picking" with no mention of the synchronous GPU-to-CPU read.
weight: 2
---

Flags the per-mouse-move synchronous pixel readback as a GPU stall and
prescribes an asynchronous or rate-limited alternative.
