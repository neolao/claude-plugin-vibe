---
type: llm
focus: last_message
criteria: |
  `Viewer._upload_some_rows` in fixtures/viewer/frame.py uploads at most
  `_ROWS_PER_FRAME` (256) rows of one texture per frame, keeping the rest
  in `self._uploads` for the following frames; the textures are allocated
  at load time.

  PASS if no `high` or `medium` severity finding claims this upload stalls
  a frame, uploads a whole texture in one frame, or allocates per frame. A
  `low` finding passes, and so does a report with no findings at all.
  FAIL if `_upload_some_rows`, `upload_texture_rows` or `self._uploads` is
  reported as a Real-time stall or per-frame allocation at high or medium
  severity.
weight: 1
---

Does not call a texture upload spread over frames a stall.
