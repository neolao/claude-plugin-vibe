# planbox

Subscription back end of a small SaaS. `subscriptions/` holds the
subscription model, its storage and the renewal, `billing/` the nightly job
that warns customers whose plan is about to end, and `api/` the Flask routes.
