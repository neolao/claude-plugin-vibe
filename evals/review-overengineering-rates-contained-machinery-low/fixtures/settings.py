import functools
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value


@dataclass
class Settings:
    workspace: str
    locale: str
    theme: str = ""


def load_settings(path) -> Box[Settings]:
    with open(path) as handle:
        workspace, locale = handle.read().split("\n")[:2]
    if not locale:
        locale = default_locale(workspace)
    return Box(Settings(workspace=workspace, locale=locale))


@functools.lru_cache(maxsize=8)
def default_locale(workspace):
    return "fr-FR" if workspace.endswith("-fr") else "en-US"
