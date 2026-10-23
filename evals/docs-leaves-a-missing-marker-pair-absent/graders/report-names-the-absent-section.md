---
type: llm
focus: last_message
criteria: |
  PASS only if the final message says that the README has no
  documentation index section (no `docs-index` marker pair, or
  equivalent wording) and that it was left absent, not added.

  FAIL if it does not mention the missing section, says the section was
  added or created, or reports that the user was asked which sections
  to add.
weight: 1
---

Step 4 reports each README section as updated, unchanged or absent; a
missing pair is the "absent" case, reported without a question.
