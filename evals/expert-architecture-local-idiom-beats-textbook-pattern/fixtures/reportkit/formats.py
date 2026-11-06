"""Output formats of `reportkit render`. Each one runs once per command, on at most a few thousand rows."""

import json

from reportkit.table import Table


def render_csv(table: Table) -> str:
    lines = [",".join(table.columns)]
    lines += [",".join(row) for row in table.rows]
    return "\n".join(lines) + "\n"


def render_json(table: Table) -> str:
    records = [dict(zip(table.columns, row)) for row in table.rows]
    return json.dumps(records, indent=2) + "\n"


FORMATS = {
    "csv": render_csv,
    "json": render_json,
}
