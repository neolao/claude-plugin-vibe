"""Admin panel endpoints. Called once per HTTP request by the threaded app server."""

from storefront import registry
from storefront.plugins.gift_wrap import GiftWrap
from storefront.plugins.loyalty import Loyalty

AVAILABLE = {"gift_wrap": GiftWrap, "loyalty": Loyalty}


def turn_off(request):
    registry.disable(request.plugin_name)
    return {"ok": True}


def turn_on(request):
    registry.enable(request.plugin_name, AVAILABLE[request.plugin_name])
    return {"ok": True}
