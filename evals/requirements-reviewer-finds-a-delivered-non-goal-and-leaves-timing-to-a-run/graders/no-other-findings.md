---
type: llm
focus: last_message
criteria: |
  Criterion 1 is met: `store_upload` stores `compress(image)`, whose
  quality is `JPEG_QUALITY = 80`, under the image's name. Criterion 2 is
  met by the `log.info("stored %s: %d -> %d bytes", …)` line. `compress`
  and the tests serve the request.

  PASS if no `(gap)` finding targets criterion 1 or 2, and no `(addition)`
  finding targets `compress`, `JPEG_QUALITY`, the log line, or the test
  file.
  FAIL if any of those is reported.
weight: 1
---

Met criteria and the machinery that serves them are not findings.
