# notifier

Sends the shop's order confirmations: the card is charged through Stripe
(`notifier/payments.py`), the mail goes out through Postal
(`notifier/mail.py`), and Stripe's webhooks are checked in
`notifier/webhooks.py`. The tests run against the stand-in for Postal that
`tests/conftest.py` starts.
