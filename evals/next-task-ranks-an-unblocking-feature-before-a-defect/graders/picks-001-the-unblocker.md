---
type: llm
focus: last_message
criteria: |
  Item 003's `depends_on` lists 001, so 001 unblocks one item; nothing
  waits on 002. Step 5's first tier is the number of items unblocked, ahead
  of defects-first.

  PASS if the presented pick is item 001.
  FAIL if it picks item 002, item 003 (not eligible: its dependency is not
  done), or reports no candidate.
weight: 3
---

Keeps the unblock count ahead of defects-first.
