---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Value object` (or clearly
  equivalent category name) finding on `Order.reroute` in
  fixtures/orders/order.py for assigning `self.shipping_address.street` in
  place instead of replacing the address, that treats `Address` as a value
  object: it names `Address`'s definition in fixtures/customers/address.py,
  or calls `Address` a value object, a mutable dataclass or a type compared
  by value. Mentioning that `PlaceOrder` hands the customer's own `Address`
  instance to the order, so the edit moves the customer too, is welcome but
  not required.
  FAIL if no finding flags the in-place edit of the address as a value-object
  issue, or if the finding says nothing about what `Address` is.
weight: 1
---

Reports `reroute` editing the `Address` value object in place as a Value
object finding. Inside the scope `Address` is only an imported name: whether
it is a value object or an entity with a lifecycle is only visible to an
agent that opens its definition outside the path given.
