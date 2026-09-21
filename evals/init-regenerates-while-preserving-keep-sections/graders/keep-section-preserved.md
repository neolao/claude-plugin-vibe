---
type: regex
target:
  source: file
  path: CLAUDE.md
pattern: "Money must never be represented as `float` in new pricing code — always convert to `Decimal` at the boundary before rounding\\. This rule predates the automated CLAUDE\\.md tooling and was agreed with finance after a rounding incident; it must survive every regeneration\\."
flags: ""
match: contains
weight: 2
---

The hand-written `## Custom section <!-- keep -->` content survives
regeneration byte-for-byte — `/vibe:init` must never touch a `<!-- keep -->`
section.
