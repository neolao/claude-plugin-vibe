"""Reads the contacts file. Called once at startup."""

TIMEOUT_SECONDS = 60


def read_contacts(path):
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()
    if not lines:
        raise ValueError(f"{path} is empty")
    return [line.split(",") for line in lines]
