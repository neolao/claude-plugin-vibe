---
type: llm
focus: last_message
criteria: |
  The fixtures use only legitimate patterns that superficially resemble
  overengineering without being one:
  - `Clock` in fixtures/clock.py has a single production implementation
    (`SystemClock`), but the seam is actually exercised by
    `FrozenClock`/`test_frozen_clock_returns_fixed_time` in the same file —
    a test seam actually used by tests, not a speculative abstraction.
  - `DiscountStrategy` in fixtures/payment_strategy.py has two concrete
    implementations (`PercentageDiscount`, `FixedAmountDiscount`) both
    actually selected at runtime in `price_order` depending on the promo
    type — a Strategy pattern with real need, not a pattern without need.
  - `HttpClientConfig.timeout_seconds` in fixtures/payment_strategy.py is set
    to different values (2 vs 30) at its two call sites for a stated reason
    (internal vs third-party latency) — configurability that is actually
    used, not unused configurability.
  - the `functools.lru_cache` on `parse_product_catalog` in
    fixtures/catalog.py is justified by a stated, plausible measured cost
    (~800ms per call, on every request) — not premature optimization.
  - the `OrderController` -> `OrderPricingService` -> `OrderRepository` split
    in fixtures/order_pricing.py separates persistence, multi-rule pricing
    logic (tax, discount, shipping), and request handling, each doing real,
    distinct work for a stated reason (pricing rules change weekly) — not
    disproportionate structure.

  PASS if the response reports no `high` or `medium` severity Speculative
  abstraction, Pattern without need, Unused configurability, Premature
  optimization, or Disproportionate structure finding on any of the five
  patterns above — either no findings at all, or only `low` severity style
  notes unrelated to them.
  FAIL if it flags `Clock` as speculative, the discount strategies as an
  unneeded pattern, the two client timeouts as unused configurability, the
  catalog cache as premature, or the pricing layering as disproportionate.
weight: 2
---

Does not invent overengineering findings on code that already follows the
idiomatic, justified pattern for each category.
