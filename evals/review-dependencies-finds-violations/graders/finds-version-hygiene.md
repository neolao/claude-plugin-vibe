---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Version hygiene` finding on the
  `left-pad` dependency in fixtures/package.json, for its wildcard `*`
  version range on a production dependency (with no lockfile committed in
  fixtures/ to pin a resolved version).
  FAIL if the `left-pad: "*"` wildcard range is not flagged.
weight: 1
---

Reports `left-pad`'s wildcard `*` version range as a Version hygiene finding.
