---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Crypto` (or clearly equivalent
  category name) finding for the share token coming from a
  non-cryptographic RNG: `tokens.share_token` (fixtures/archiver/tokens.py)
  calls `ids.short_id(24)`, which (fixtures/archiver/ids.py) uses
  `random.choices`, and the partner portal hands a document to anyone who
  presents that token, so an attacker who observes enough outputs can
  predict the next tokens. The finding may be anchored in ids.py or
  tokens.py, as long as it names the share token.
  A finding that only says `short_id` uses `random`, without tying it to the
  share token or any security use, does not count.
  FAIL if no finding flags this weak token.
weight: 1
---

Reports the share token built by `random.choices`. tokens.py alone calls an
id helper; only ids.py shows which RNG it uses.
