from report_renderer import render_report


def archive_report(report, path):
    """Called after every report is sent, for the audit trail."""
    with open(path, "w") as handle:
        handle.write(render_report(report, fmt="plain"))
