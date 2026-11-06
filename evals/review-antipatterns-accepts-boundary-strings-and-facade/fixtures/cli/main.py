"""Command-line entry point of the export tool."""

import argparse
import os

from cli.settings import Environment, OutputFormat
from cli.export import run_export


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=[f.value for f in OutputFormat], default="text")
    return parser.parse_args(argv)


def main(argv):
    environment = Environment(os.environ.get("APP_ENV", "development"))
    output_format = OutputFormat(parse_args(argv).format)
    return run_export(environment, output_format)
