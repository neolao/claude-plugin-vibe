---
type: llm
focus: last_message
criteria: |
  During the rollout, five pods still running the old version and the
  checkout (deployed days later by another team) read `price:<sku>` and
  expect a bare number; a pod already on the new version writes the
  structured entry under the same key.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS says that the old pods and
  the checkout must keep reading a price while new-format entries are being
  written, and prescribes how: the structured entry written under a new
  key or key space (`price:v2:<sku>`) while the bare number keeps being
  written under the old key until every reader has moved, or readers
  updated to accept either format before any writer switches — with a
  stated behaviour or a test scenario for an old reader meeting a new
  entry.
  FAIL if the reply treats the change as a one-step switch (write the new
  format, deploy) with no word on the pods and the checkout still expecting
  a bare number under the same key.
weight: 2
---

Requires the old pods and the separately deployed checkout to keep reading
a price while the new format is being written.
