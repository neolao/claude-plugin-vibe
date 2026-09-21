---
type: regex
target: last_message
pattern: "REQUIREMENTS:.*RISKS:.*TEST SCENARIOS:"
flags: is
weight: 1
---

The reply follows the REQUIREMENTS: / RISKS: / TEST SCENARIOS: contract instead of
free-form prose.
