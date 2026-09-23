---
type: regex
target: last_message
pattern: "(?:^|\\n)[#*_ \\t]*REQUIREMENTS[*_]*:?[*_]*\\s[\\s\\S]*\\n[#*_ \\t]*RISKS[*_]*:?[*_]*\\s[\\s\\S]*\\n[#*_ \\t]*TEST SCENARIOS[*_]*:?[*_]*\\s"
flags: i
weight: 1
---

The reply follows the requested three-bulleted-list format (REQUIREMENTS /
RISKS / TEST SCENARIOS headers, in order) instead of free-form prose.

Each label starts a line; a markdown heading or emphasis around it (`## RISKS`,
`**RISKS:**`) still counts, as the invoking skill reads it the same way.
