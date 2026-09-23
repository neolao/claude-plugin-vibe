---
type: llm
focus: last_message
criteria: |
  `HttpClientConfig` groups a base URL and a timeout that both differ between
  `build_internal_client` (internal host, 2s) and `build_external_client`
  (payment gateway, 30s, for a stated latency reason); `fetch` reads both
  fields on both paths (`sync_inventory` and `fetch_payment_status`).

  PASS if no `high` or `medium` severity finding (Unused configurability,
  Pattern without need or Speculative abstraction) targets `HttpClientConfig`
  or its two builders.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a parameter that genuinely varies unused configurability.
