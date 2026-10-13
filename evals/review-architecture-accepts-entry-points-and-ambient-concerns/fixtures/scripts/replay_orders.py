"""Replays orders from a JSON-lines file: python scripts/replay_orders.py orders.jsonl"""

import json
import sys

from main import build_order_service


def main(path):
    service = build_order_service()
    with open(path) as handle:
        for line in handle:
            service.place_order(json.loads(line))


if __name__ == "__main__":
    main(sys.argv[1])
