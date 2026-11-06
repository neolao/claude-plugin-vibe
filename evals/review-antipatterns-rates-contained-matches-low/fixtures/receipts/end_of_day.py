"""End-of-day job."""

from receipts.report import Report


def run(store, day):
    report = Report(store)
    report.load(day)
    return report.render()
