---
type: llm
focus: last_message
criteria: |
  fixtures/exporter/client.py reads `# partner answers 200 with an empty
  body when throttling (their ticket PRT-418): retryable` above
  `if not body: raise Throttled()`. The code shows the check and the raise;
  that an empty 200 means throttling is the partner's behaviour, which no
  file in the repository can confirm or deny.

  PASS if no `high` or `medium` severity finding calls that comment
  misleading or redundant, and no finding at any severity asks to delete
  it. A `low` finding that only shortens its wording passes, as does a
  report with no findings at all.
  FAIL if the comment is flagged at high or medium severity as Misleading
  or Redundant (or equivalent), or if a finding suggests deleting it.
weight: 1
---

Keeps a why the repository cannot check: the external behaviour the
comment explains is exactly what the code cannot show.
