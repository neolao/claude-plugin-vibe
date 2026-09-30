---
type: tool_used
tool: Edit
input_match: "src/pricing\\.js"
min: 0
max: 0
weight: 2
---

The reported symptom is on `orderTotal`, but that function only forwards to
the shared helper. A fix that edits `src/pricing.js` patches a symptom and
leaves the same defect in `lineTotal` and `applyDiscount`.
