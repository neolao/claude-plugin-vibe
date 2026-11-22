"""Called from the checkout endpoint for every order."""

from storefront import registry


def price(cart):
    for extension in registry.active():
        extension.adjust(cart)
    return cart.total()
