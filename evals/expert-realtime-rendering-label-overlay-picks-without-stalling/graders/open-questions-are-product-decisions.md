---
type: llm
focus: last_message
criteria: |
  The request allows a fourth list, `OPEN QUESTIONS:` (≤3), only for a real
  product decision in the expert's domain, phrased for a non-technical
  Product Owner. `/vibe:feature` puts these straight to the user in plain
  words, so a technical question reaches the wrong person.

  PASS if the reply either has no `OPEN QUESTIONS:` list, or lists at most 3
  questions that are genuine business choices answerable by someone who does
  not read code (for example whether labels of far-away objects may be
  hidden, or whether hovering a thin object must be pixel-exact or may be
  slightly forgiving).
  FAIL if it asks the caller to settle a technical detail the expert could
  decide itself (the frame budget, the label batching method, the atlas
  size, a texture format, whether to read back asynchronously, how often to
  run the picking pass, whether a hover highlight may arrive a frame or two
  late), or phrases a question in terms a non-technical
  Product Owner could not answer.
weight: 1
---

Keeps `OPEN QUESTIONS:` for real product decisions phrased for a
non-technical Product Owner — or omits the list entirely.
