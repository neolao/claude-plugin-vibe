import os


def inside(root, name):
    target = os.path.join(root, name)
    if not target.startswith(root):
        raise ValueError(f"{name} is outside {root}")
    return target
