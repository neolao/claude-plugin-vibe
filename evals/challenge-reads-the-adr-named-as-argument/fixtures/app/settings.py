"""Runtime settings of the desktop app, read from config/app.toml next to the binary."""
import tomllib
from pathlib import Path


def load(root: Path) -> dict:
    with open(root / "config" / "app.toml", "rb") as settings_file:
        return tomllib.load(settings_file)
