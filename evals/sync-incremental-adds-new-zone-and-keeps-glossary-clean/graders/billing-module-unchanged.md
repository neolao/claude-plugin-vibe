---
type: llm
focus: { source: file, path: ".vibe/modules/billing.md" }
criteria: |
  The file's content must be EXACTLY identical, character for character
  (including line breaks and spacing), to this reference text:

  # Module: billing
  **Role:** Charges a customer for a given amount.
  **Files:** `src/billing/index.js`
  **Exports:** `charge(customerId, amountCents): { customerId, amountCents, status }`
  **Depends on:** (none)

  PASS only if the file matches this reference exactly, with no added,
  removed, reordered, or reworded lines.
  FAIL on any deviation, however small — including a merely equivalent
  rewording.
weight: 2
---

`src/billing/` was never touched, so `.vibe/modules/billing.md` must stay
byte-for-byte unchanged — the whole point of incremental mode is scoping
only to what changed (precision).
