import json
import re
from dataclasses import dataclass, field
from pathlib import Path

ENTRY_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")


@dataclass
class Entry:
    name: str


@dataclass
class Listing:
    site: str
    entries: list = field(default_factory=list)


def read(staging_dir):
    raw = json.loads(Path(staging_dir, "MANIFEST").read_text())
    entries = []
    for name in raw["entries"]:
        if not isinstance(name, str) or not ENTRY_NAME.match(name):
            raise ValueError(f"invalid entry name: {name!r}")
        entries.append(Entry(name=name))
    return Listing(site=str(raw["site"]), entries=entries)
