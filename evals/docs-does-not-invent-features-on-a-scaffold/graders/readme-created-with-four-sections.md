---
type: regex
target: { source: file, path: README.md }
pattern: "vibe:begin:features[\\s\\S]*vibe:end:features[\\s\\S]*vibe:begin:install[\\s\\S]*vibe:end:install[\\s\\S]*vibe:begin:usage[\\s\\S]*vibe:end:usage[\\s\\S]*vibe:begin:docs-index[\\s\\S]*vibe:end:docs-index"
weight: 1
---

No README existed: the skill creates one with the four managed sections
(Step 2, "No README").
