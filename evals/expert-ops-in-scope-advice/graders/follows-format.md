---
type: regex
target: last_message
pattern: "REQUIREMENTS:[\\s\\S]*RISKS:[\\s\\S]*TEST SCENARIOS:"
flags: i
weight: 1
---

The reply follows the requested three-bulleted-list format (REQUIREMENTS /
RISKS / TEST SCENARIOS headers, in order) instead of free-form prose.
