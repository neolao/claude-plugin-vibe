import os

import stripe

STRIPE_KEY = os.environ.get("STRIPE_KEY", "sk_test_FAKE51Hq3LmZq9Xy2VbNqR7tWe")


def charge(card_token, amount_cents):
    stripe.api_key = STRIPE_KEY
    return stripe.Charge.create(amount=amount_cents, currency="eur", source=card_token)
