# planbox

Subscription back end of a small SaaS. `subscriptions/` holds the
subscription model, its storage and the renewal use case, `billing/` the
monthly statement built from the payment gateway's export, and `api/` the
Flask routes and the shapes the account page reads.
