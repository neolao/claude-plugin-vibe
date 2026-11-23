"""Shipping cost shown at checkout."""


# TODO(#88): costs come from a hard-coded table until the carrier client is
# available; do not call the carrier API from here yet.
def shipping_cost(order, carrier):
    return carrier.quote(weight_grams=order.weight_grams, country=order.country)
