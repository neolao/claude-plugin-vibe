---
type: llm
focus: last_message
criteria: |
  Creating the GPU texture for a full-resolution PNG is an upload to the GPU
  that WebGL performs on the main thread; a large texture uploaded whole in
  the frame the object comes within range costs that frame tens of
  milliseconds on a laptop, and several objects crossing the threshold
  together multiply it.

  PASS if REQUIREMENTS or RISKS names the GPU texture creation (the upload
  to the GPU, `texImage2D` or an equivalent) as per-frame cost in its own
  right, distinct from the download and decode, and requires it to be
  bounded: spread across frames (one texture or a budgeted number of bytes
  per frame, mip levels or tiles over several frames), or a cap on how many
  streamed textures are created in a single frame.
  FAIL if the reply treats the texture as ready to draw once decoded, never
  mentions the GPU upload as a cost of its own, or mentions it without
  requiring it to be spread or capped per frame.
weight: 2
---

Treats the GPU texture upload as a per-frame cost distinct from decode and
requires it spread or capped per frame.
