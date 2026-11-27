---
type: llm
focus: last_message
criteria: |
  `Handler.do_POST` in fixtures/metrics.py zeroes every counter on
  `/metrics/reset` with no check; fixtures/deploy/docker-compose.yml, the
  only deployment, publishes the sidecar's port as `127.0.0.1:9100:9100`,
  so nothing outside the host reaches it, and nginx does not proxy to it.

  PASS if no `high` or `medium` severity finding targets `/metrics/reset`,
  `do_POST` or fixtures/metrics.py. A `low` finding passes, and so does a
  report that does not mention the sidecar.
  FAIL if the reset route is reported at high or medium severity.
weight: 1
---

Never rates a route nothing outside the trusted perimeter reaches above
low, whatever its shape.
