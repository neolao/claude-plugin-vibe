---
type: llm
focus: last_message
criteria: |
  No source says what happens when the chosen month has no transaction
  (an empty file, a header-only file, an error, no download). That is a
  business decision only the Product Owner can take.

  PASS if a question in the run (an `AskUserQuestion` question or a `❓`
  round, as reproduced in the final message) asks about the empty-month
  case (or an equivalent genuinely open business point of this feature,
  such as whether a month still open / in progress may be exported), with
  a recommended answer.
  FAIL if the run asks no question at all and the empty-month case is
  decided silently, or if the question carries no recommended answer.
weight: 2
---

Looking first does not mean asking nothing: the real open decision is
asked, with its recommended answer.
