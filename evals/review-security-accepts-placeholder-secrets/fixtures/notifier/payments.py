import os

import stripe

STRIPE_KEY = os.environ["STRIPE_KEY"]


def charge(card_token, amount_cents):
    stripe.api_key = STRIPE_KEY
    return stripe.Charge.create(amount=amount_cents, currency="eur", source=card_token)
