class ReportService:
    def __init__(self, repository):
        self._repository = repository

    def title(self, report_id):
        return self._repository.fetch(report_id)["title"]
