---
type: llm
focus: last_message
criteria: |
  `HttpClientConfig.timeout_seconds` is 2 in `build_internal_client` and 30
  in `build_external_client`, for a stated latency reason.

  PASS if no `high` or `medium` severity Unused configurability finding
  targets it.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a parameter that genuinely varies unused configurability.
