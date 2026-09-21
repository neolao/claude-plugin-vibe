---
type: regex
target: last_message
pattern: "FILE:.*\\n?.*CATEGORY:.*\\n?.*SEVERITY:\\s*(high|medium|low)"
flags: is
weight: 1
---

At least one finding follows the FILE/CATEGORY/SEVERITY/ISSUE/SUGGESTION contract
instead of free-form prose.
