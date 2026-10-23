---
type: regex
target:
  source: file
  path: roadmap/.vibe/decisions/001-one-repo-owns-orders.md
pattern: "^---\\nstatus: accepted\\ndate: 2026-09-14\\n---\\n# 001 — One repo owns the orders domain\\n\\n## Context\\nTwo repos were writing order records\\.\\n\\n## Decision\\n`orders-api` owns the `orders` domain; every other repo reads it through the API\\.\\n\\n## Consequences\\nThe storefront drops its local order table\\.\\n$"
flags: ""
match: contains
weight: 2
---

The hub's existing ADR is byte for byte what the fixture wrote: the
refresh touches no ADR.
