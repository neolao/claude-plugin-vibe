---
type: llm
focus: last_message
criteria: |
  `fetch_json` in fixtures/client.py wraps `http_get` and adds a default
  timeout, JSON decoding, and translation of low-level errors into
  `FetchError`. It is an adaptation, not a pure delegation.

  PASS if no finding calls `fetch_json` (or `http_get`) a pointless wrapper,
  a forwarding function, or asks to inline or remove it.
  FAIL if `fetch_json` is reported as `Indirection` (or equivalent) or is
  suggested for removal or inlining.
weight: 1
---

Does not flag a wrapper that adds a default, decoding and error translation.
