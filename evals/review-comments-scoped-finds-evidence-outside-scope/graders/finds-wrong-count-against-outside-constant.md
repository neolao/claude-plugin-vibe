---
type: llm
focus: last_message
criteria: |
  fixtures/sync/poller.py reads `attempts = MAX_ATTEMPTS  # 3 tries, then
  give up`; `MAX_ATTEMPTS` is defined as `5` in fixtures/config/settings.py,
  outside the scope.

  PASS if the reported findings include a `Misleading` (or clearly
  equivalent category name) finding on that comment in
  fixtures/sync/poller.py whose ISSUE or SUGGESTION says the real value is 5
  (or names `MAX_ATTEMPTS` / fixtures/config/settings.py as the
  contradiction).
  FAIL if no finding flags the comment as misleading, or if the finding
  never says what contradicts it.
weight: 1
---

Reports the `# 3 tries` comment as `Misleading`, with the outside constant
as evidence. Inside fixtures/sync/ nothing says what `MAX_ATTEMPTS` is worth:
only an agent that greps the whole repository can tell the comment lies.
