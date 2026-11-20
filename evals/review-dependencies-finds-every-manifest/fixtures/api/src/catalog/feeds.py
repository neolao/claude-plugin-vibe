"""Supplier feeds arrive as YAML files uploaded by the suppliers themselves."""
import yaml


def load_feed(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as handle:
        document = yaml.load(handle, Loader=yaml.FullLoader)
    return document.get("products", [])
