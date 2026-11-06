"""Command-line entry point of the export tool."""

import os

from cli.export import run_export


def main():
    environment = os.environ.get("APP_ENV", "development")
    return run_export(environment)
