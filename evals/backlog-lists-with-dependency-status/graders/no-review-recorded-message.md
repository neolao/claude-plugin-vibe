---
type: regex
target: last_message
pattern: "No review recorded yet"
flags: i
weight: 1
---

Since `.vibe/last-review.md` doesn't exist in the fixture, reports the "No
review recorded yet" message instead of a review date/commit.
