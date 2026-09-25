---
type: regex
target:
  source: file
  path: CLAUDE.md
pattern: "`vibe:review-web-security` \\| ✅ \\|"
flags: ""
match: contains
weight: 1
---

`src/shop_api/app.py` exposes FastAPI routes, so the stale
`❌ | no HTTP surface` row becomes `✅`. The user declined dynamic
probing, so it is plain `✅`, not `✅ (dynamic)`.
