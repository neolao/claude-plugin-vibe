---
type: llm
focus: last_message
criteria: |
  `Viewer.frame` in fixtures/viewer/frame.py opens, reads and parses
  `camera.json` from disk at the top of every frame.

  PASS if exactly one finding targets that read (`open("camera.json")` /
  `json.load`), its category is `Blocking` (or a clearly equivalent name),
  and no other finding — in particular none under `Real-time` — reports
  the same read, parse or file.
  FAIL if no finding reports the per-frame file read, if its category is
  `Real-time`, or if a second finding reports the same read under another
  category.
weight: 2
---

Reports synchronous I/O and parsing inside the frame as Blocking, once:
never a second finding on the same line under Real-time.
