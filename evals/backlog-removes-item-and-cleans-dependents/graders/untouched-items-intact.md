---
type: llm
focus: { source: file, path: ".vibe/backlog/003-send-receipt-emails.md" }
criteria: |
  PASS if the file is still the item 003, `Send Receipt Emails`, with
  `status: todo`, no `depends_on` line and its two acceptance criteria.
  FAIL if it was changed in any way.
weight: 1
---

003 is not a dependent of 001 and must not be touched.
