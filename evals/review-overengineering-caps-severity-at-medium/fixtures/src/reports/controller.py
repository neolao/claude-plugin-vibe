class ReportController:
    def __init__(self, service):
        self._service = service

    def handle(self, report_id):
        return self._service.title(report_id)
