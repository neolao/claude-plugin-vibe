import plugins.csv_import  # noqa: F401  registers the plugin
from plugins.registry import load


def run_import(path):
    """Entry point of the import command."""
    with open(path) as handle:
        return load("csv").rows(handle)
