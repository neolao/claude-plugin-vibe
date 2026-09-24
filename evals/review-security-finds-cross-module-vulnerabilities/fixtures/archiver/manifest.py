from dataclasses import dataclass, field
from pathlib import Path

from . import serializer


@dataclass
class Entry:
    name: str


@dataclass
class Listing:
    site: str
    entries: list = field(default_factory=list)


def read(staging_dir):
    blob = Path(staging_dir, "MANIFEST").read_bytes()
    return serializer.decode(blob)


def write(staging_dir, listing):
    Path(staging_dir, "MANIFEST").write_bytes(serializer.encode(listing))
