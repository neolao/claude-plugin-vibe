---
type: regex
target: last_message
pattern: "REQUIREMENTS:[\\s\\S]*RISKS:[\\s\\S]*TEST SCENARIOS:"
flags: i
weight: 1
---

The reply follows the three-list contract (REQUIREMENTS / RISKS / TEST
SCENARIOS) instead of free-form prose.
