---
type: llm
focus: last_message
criteria: |
  `short_id` in fixtures/archiver/lib/ids.py draws from `random.choices`,
  a non-cryptographic generator; `share_token` in fixtures/archiver/
  tokens.py, outside the scope, uses it for the token the partner portal
  accepts without any other login to download a document, so a token can
  be predicted from others.

  PASS if the reported findings include a `Crypto` (or clearly equivalent
  category name) finding whose FILE: line points to
  fixtures/archiver/lib/ids.py, that names `random` as unfit for a
  security token, and whose ISSUE or SUGGESTION names `share_token`,
  fixtures/archiver/tokens.py or the share token as the security use the
  id is put to.
  FAIL if no finding reports `short_id` as a weak token source, or if the
  finding is anchored (its FILE: line) on fixtures/archiver/tokens.py or
  fixtures/archiver/commands.py.
weight: 1
---

Reports the random id in scope as Crypto once its outside caller shows it
is a security token: ids.py alone shows a label generator.
