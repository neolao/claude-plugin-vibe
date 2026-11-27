from report_renderer import render_report


def send_weekly_report(report, mailer):
    """Called every Monday by the reporting job."""
    mailer.send("management@example.com", render_report(report, fmt="plain"))
