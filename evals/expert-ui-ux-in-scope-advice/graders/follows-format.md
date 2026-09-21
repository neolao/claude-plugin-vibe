---
type: regex
target: last_message
pattern: "REQUIREMENTS:[\\s\\S]*RISKS:[\\s\\S]*TEST SCENARIOS:"
flags: i
weight: 1
---

The reply follows the REQUIREMENTS: / RISKS: / TEST SCENARIOS: contract instead of
free-form prose.
