---
type: llm
focus: last_message
criteria: |
  The plan fetches the PNG and decodes it at the moment an object first comes
  within range, while the camera keeps moving: a synchronous fetch or a PNG
  decode on the main thread at that moment stalls the frame in which the
  object crosses the threshold.

  PASS if REQUIREMENTS or RISKS ties the fetch and decode of a streamed
  texture to the render loop and requires them off it: an asynchronous fetch
  with the decode on a worker or through the browser's asynchronous image
  decoding (`createImageBitmap` or an equivalent), or the texture requested
  and decoded ahead of range so nothing is decoded in the frame the object
  becomes close — with the result handed to the loop only once ready.
  FAIL if the reply never raises the fetch or decode happening on the loop at
  the moment the object comes within range, or covers it only as a generic
  "avoid blocking I/O" statement with no tie to the streaming moment the
  brief describes.
weight: 2
---

Keeps the fetch and PNG decode of a streamed texture off the render loop,
anchored on the moment the object first comes within range.
