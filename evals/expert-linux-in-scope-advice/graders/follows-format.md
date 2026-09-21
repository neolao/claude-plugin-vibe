---
type: regex
target: last_message
pattern: "REQUIREMENTS:.*\\n?.*RISKS:.*\\n?.*TEST SCENARIOS:"
flags: is
weight: 1
---

The reply follows the requested three-list contract (REQUIREMENTS / RISKS /
TEST SCENARIOS) instead of free-form prose.
