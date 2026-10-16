---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Ubiquitous language` (or clearly
  equivalent category name) finding on a file under fixtures/orders/ for
  calling the customer a `buyer` (`Order.buyer_id`,
  `OrderRepository.find_for_buyer`, the `buyer_id` column) while the rest of
  the repository calls the same person a customer, and that names at least
  one of those outside files: `Customer.customer_id` in
  fixtures/customers/customer.py, `PlaceOrder` in
  fixtures/checkout/place_order.py handing `customer.customer_id` to `Order`,
  `CustomerOrders.for_customer` in fixtures/checkout/customer_orders.py or
  the `/customers/<customer_id>/orders` route in fixtures/api/routes.py
  feeding `customer_id` into `find_for_buyer`. Which of the two names the
  finding proposes to keep does not matter.
  FAIL if no finding flags the `buyer` / `customer` split for the same
  concept, or if the finding names no file outside fixtures/orders/.
weight: 1
---

Reports the orders package naming the customer a `buyer` as a Ubiquitous
language finding, against the `customer` vocabulary of the packages around
it. Inside the scope the name is consistent: the drift is only visible to an
agent that reads the other layers.
