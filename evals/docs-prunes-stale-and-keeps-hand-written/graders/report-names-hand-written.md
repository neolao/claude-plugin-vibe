---
type: llm
focus: last_message
criteria: |
  PASS only if the final message mentions `docs/contributing.md` as a
  hand-written file (no generated banner) that was left alone.

  FAIL if it does not mention `docs/contributing.md`, or says it was
  modified or regenerated.
weight: 1
---

Step 4 reports any hand-written `docs/` file left alone.
