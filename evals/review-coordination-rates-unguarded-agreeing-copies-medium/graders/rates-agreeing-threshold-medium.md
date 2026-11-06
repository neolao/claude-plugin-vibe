---
type: llm
focus: last_message
criteria: |
  The free-shipping threshold is written twice: `FREE_SHIPPING_THRESHOLD =
  50.0` in fixtures/pricing/fees.py and the literal `50.0` (twice) in
  `shipping_banner` of fixtures/web/cart_view.py, under a `# keep in sync
  with pricing/fees.py` comment. The two values are equal today; nothing
  imports one from the other, no test compares them, no runtime check
  exists.

  PASS if the reported findings include a finding on that threshold
  (anchored on fixtures/web/cart_view.py or fixtures/pricing/fees.py, in
  category `Copied constant`, `Restated rule` or `Confessed coordination`,
  or a clearly equivalent name) with SEVERITY `medium`.
  FAIL if no finding names the two copies of the threshold, or if that
  finding carries SEVERITY `high` or `low`.
weight: 2
---

Rates copies that agree today, with no guard and a describable next change
(raising the threshold in fees.py and leaving the banner at 50), at
`medium`: they produce no wrong result yet, so `high` is wrong, and the
"keep in sync" comment is not a reason to drop to `low`.
