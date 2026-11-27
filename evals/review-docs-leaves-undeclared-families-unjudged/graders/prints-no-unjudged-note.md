---
type: regex
target: last_message
pattern: "unjudged|not judged|no template (was )?(found|declared|transmitted)"
match: not_contains
flags: i
weight: 1
---

No note about families left unjudged reaches the output: the review brick
relays findings, not notes, and a family with no declared template is
passed over in silence.
