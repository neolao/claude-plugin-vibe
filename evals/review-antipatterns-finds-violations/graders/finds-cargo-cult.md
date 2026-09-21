---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Cargo cult` (or clearly
  equivalent category name) finding on the `REDIS_POOL_SIZE` /
  `REDIS_SOCKET_TIMEOUT` / `REDIS_RETRY_ON_TIMEOUT` constants in
  fixtures/config.py, for leftover template configuration with no Redis
  usage anywhere in the codebase.
  FAIL if no finding flags these unused Redis constants.
weight: 1
---

Reports the unused Redis config constants in fixtures/config.py as a Cargo
cult finding.
