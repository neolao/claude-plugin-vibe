---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Ubiquitous language` (or clearly
  equivalent category name) finding on `fixtures/order_routes.py`, for
  calling the customer a `user` (`/users/<user_id>`, the `user_id`
  parameter passed straight into `repo.find_for_customer(user_id)`) while
  the rest of the domain in scope — `Order.customer_id`,
  `OrderRepository.find_for_customer`, the `customer_id` column — calls the
  same concept a customer. One concept, two names, with the route layer
  being the one that drifts.
  FAIL if no finding flags the `user` / `customer` split for the same
  concept.
weight: 1
---

Reports the route layer naming the customer a `user`, against the
`customer_id` vocabulary the rest of the code in scope uses, as a
`Ubiquitous language` finding.
