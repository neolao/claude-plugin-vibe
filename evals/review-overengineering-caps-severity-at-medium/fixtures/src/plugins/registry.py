_PLUGINS = {}


def register(name):
    def decorator(cls):
        _PLUGINS[name] = cls
        return cls

    return decorator


def load(name):
    return _PLUGINS[name]()
