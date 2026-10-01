---
type: llm
focus: { source: file, path: ".vibe/modules/shipping.md" }
criteria: |
  PASS if the file exists and documents a shipping module: it lists
  `src/shipping/index.js` as a file and names both the `createShipment` and
  `dispatch` exports.
  FAIL if the file is missing, or omits either export.
weight: 2
---

The new uncommitted zone src/shipping/ must get its own module doc (recall).
