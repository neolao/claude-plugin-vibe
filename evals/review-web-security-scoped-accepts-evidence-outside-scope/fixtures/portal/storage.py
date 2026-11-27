"""File helpers for uploads and exports."""

import os

UPLOAD_DIR = os.path.realpath("/var/data/uploads")


def upload_path(name):
    """Location of a previously uploaded attachment."""
    target = os.path.realpath(os.path.join(UPLOAD_DIR, name))
    if not target.startswith(UPLOAD_DIR + os.sep):
        raise FileNotFoundError(name)
    return target


def render_export(rows):
    """Renders the first `rows` activity lines as CSV."""
    lines = []
    for i in range(rows):
        lines.append(f"{i},activity")
    return "\n".join(lines)
