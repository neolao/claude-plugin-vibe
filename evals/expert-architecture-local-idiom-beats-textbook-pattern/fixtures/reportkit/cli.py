"""Command line of reportkit: `reportkit render <file> --format <name>`."""

import argparse
import sys

from reportkit.formats import FORMATS
from reportkit.table import Table


def load(path: str) -> Table:
    with open(path) as f:
        header, *rows = [line.rstrip("\n").split("\t") for line in f]
    return Table(header, rows)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="reportkit")
    sub = parser.add_subparsers(dest="command", required=True)
    render = sub.add_parser("render")
    render.add_argument("file")
    render.add_argument("--format", choices=sorted(FORMATS), default="csv")
    args = parser.parse_args(argv)
    sys.stdout.write(FORMATS[args.format](load(args.file)))
    return 0
