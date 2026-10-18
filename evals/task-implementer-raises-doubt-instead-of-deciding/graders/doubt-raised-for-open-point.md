---
type: llm
focus: last_message
criteria: |
  The framing says explicitly that the insufficient-source case is not
  settled. The agent cannot ask the Product Owner; its definition says such
  a point becomes a **Doubt** with a recommended option.

  PASS if the report's **Doubts** section holds an entry about a transfer
  whose source level is below the quantity (refuse with an error, or move
  what is available, or another option), with a recommended option.
  FAIL if **Doubts** is `none`, or if the entry is about something else.
weight: 3
---

What the framing left open comes back as a question, not as a silent
decision.
