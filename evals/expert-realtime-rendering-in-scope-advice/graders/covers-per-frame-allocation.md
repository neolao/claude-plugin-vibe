---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS or RISKS specifically flags that spawning a new burst
  of particle instances every frame for each selected object risks
  per-frame heap allocation, and requires reusing a pre-allocated
  pool/buffer of particle instances across frames instead of allocating new
  ones each frame. A generic "optimize performance" or "use object pooling"
  statement with no tie to the per-frame particle spawn described in the
  brief does not count.
  FAIL if the per-frame allocation risk of the particle spawn is absent or
  only stated as a generic platitude.
weight: 2
---

Flags the per-frame particle spawn as a heap-allocation risk and requires
reusing buffers/objects across frames.
