"""Called when a request arrives for a different shop than the previous one."""

from storefront import registry


def switch_to(tenant):
    for name in tenant.disabled_plugins:
        registry.disable(name)
