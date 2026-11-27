from exports.container import build_container


def run_export(rows, path):
    """Entry point of the weekly accounting export."""
    exporter = build_container().resolve("exporter")
    exporter.write(rows, path)
