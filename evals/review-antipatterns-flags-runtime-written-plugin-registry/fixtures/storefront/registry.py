"""Plugin registry for the storefront.

Plugin modules register themselves with the decorator below when
storefront.plugins is imported.
"""

_PLUGINS = {}


def plugin(name):
    def decorate(cls):
        _PLUGINS[name] = cls()
        return cls
    return decorate


def disable(name):
    _PLUGINS.pop(name, None)


def enable(name, cls):
    _PLUGINS[name] = cls()


def active():
    return list(_PLUGINS.values())
