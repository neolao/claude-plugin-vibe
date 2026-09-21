---
type: regex
target: last_message
pattern: "PACKAGE:.*\\n?.*CATEGORY:.*\\n?.*SEVERITY:\\s*(high|medium|low)"
flags: is
weight: 1
---

At least one finding follows this agent's own contract override —
`PACKAGE: name@version (manifest)` in place of `FILE:`, followed by
CATEGORY/SEVERITY/ISSUE/SUGGESTION — instead of free-form prose or the
generic `FILE:` form.
