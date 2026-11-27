class ReportRepository:
    def __init__(self, reports):
        self._reports = reports

    def fetch(self, report_id):
        return self._reports.get(report_id)
