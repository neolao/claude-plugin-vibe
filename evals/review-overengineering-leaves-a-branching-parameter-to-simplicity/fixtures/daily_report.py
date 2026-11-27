from report_renderer import render_report


def send_daily_report(report, mailer):
    """Called once a day by the reporting job."""
    mailer.send("ops@example.com", render_report(report, fmt="plain"))
