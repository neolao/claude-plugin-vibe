---
type: regex
target: { source: file, path: ".vibe/last-review.md" }
pattern: "date:\\s*\\d{4}-\\d{2}-\\d{2}[\\s\\S]*commit:\\s*[0-9a-f]{7,40}"
flags: i
weight: 1
---

`.vibe/last-review.md` must follow the Step 6 template exactly — a `date:`
line (YYYY-MM-DD) followed by a `commit:` line naming the resulting HEAD hash
— not just exist as an empty or unrelated file.
