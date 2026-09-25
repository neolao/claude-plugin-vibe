---
type: regex
target:
  source: file
  path: CLAUDE.md
pattern: "`vibe:review-ddd` \\| ✅ \\|"
flags: ""
match: contains
weight: 1
---

`src/shop_api/domain/order.py` is an explicit domain layer, so the stale
`❌ | no explicit domain model` row becomes `✅`.
