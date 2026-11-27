"""File helpers for uploads and exports."""

import os

UPLOAD_DIR = "/var/data/uploads"


def upload_path(name):
    """Location of a previously uploaded attachment."""
    return os.path.join(UPLOAD_DIR, name)


def render_export(rows):
    """Renders the first `rows` activity lines as CSV."""
    lines = []
    for i in range(rows):
        lines.append(f"{i},activity")
    return "\n".join(lines)
