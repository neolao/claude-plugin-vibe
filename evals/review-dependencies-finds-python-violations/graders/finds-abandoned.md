---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Abandoned` finding on
  `pycrypto` in fixtures/pyproject.toml, noting it is unmaintained and
  suggesting a replacement such as `pycryptodome` or `cryptography`. A
  `Vulnerability` finding on `pycrypto` in addition is fine.
  FAIL if `pycrypto` is not flagged as abandoned/unmaintained.
weight: 1
---

Reports the unmaintained `pycrypto` as an Abandoned finding.
