"""The export itself."""

import json

from cli.settings import Environment, OutputFormat


def run_export(environment, output_format):
    rows = _load_rows(environment)
    if output_format is OutputFormat.JSON:
        return json.dumps(rows)
    return "\n".join(",".join(row) for row in rows)


def _load_rows(environment):
    if environment is Environment.PRODUCTION:
        return [["order", "1"]]
    return [["order", "sample"]]
