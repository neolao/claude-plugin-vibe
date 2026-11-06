"""The export itself."""

from cli.alerts import notify
from cli.storage import rows_for


def run_export(environment):
    rows = rows_for(environment)
    if environment == "production":
        notify(environment, len(rows))
    return "\n".join(",".join(row) for row in rows)
