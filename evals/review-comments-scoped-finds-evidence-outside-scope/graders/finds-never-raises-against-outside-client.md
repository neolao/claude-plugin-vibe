---
type: llm
focus: last_message
criteria: |
  fixtures/sync/poller.py reads `batch = fetch_pending()  # never raises:
  the client swallows HTTP errors and returns []`; `fetch_pending` in
  fixtures/gateway/client.py, outside the scope, raises `RuntimeError` on a
  4xx/5xx status and swallows nothing.

  PASS if the reported findings include a `Misleading` (or clearly
  equivalent category name) finding on that comment in
  fixtures/sync/poller.py that names the `raise` (or `RuntimeError`, or
  fixtures/gateway/client.py) as the contradiction.
  FAIL if no finding flags the comment as misleading, or if the finding
  never says what contradicts it.
weight: 1
---

Reports the `# never raises` comment as `Misleading`, with the outside
client as evidence: the function the comment describes sits outside the
scope and must be read there.
