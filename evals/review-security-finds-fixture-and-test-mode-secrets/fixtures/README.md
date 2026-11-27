# notifier

Sends the shop's order confirmations: the card is charged through Stripe
(`notifier/payments.py`), the mail goes out through Postal
(`notifier/mail.py`), and Stripe's webhooks are checked in
`notifier/webhooks.py`. `tests/test_mail.py` runs against Postal's sandbox
account, whose key is in `tests/fixtures/postal_account.yaml`.
