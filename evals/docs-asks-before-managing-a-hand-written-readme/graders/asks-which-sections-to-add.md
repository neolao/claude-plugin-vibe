---
type: llm
focus: last_message
criteria: |
  PASS only if the final message carries or relays a question to the
  user about which README sections to put under management (or to add),
  naming at least two of: features, installation, usage, documentation
  index.

  FAIL if the message reports the sections as added, inserted or
  updated, reports them as absent without a question, or says nothing
  about managed sections.
weight: 2
---

A README without any managed section is the one case where the skill
asks: it lists the sections it could manage and waits for the answer.
