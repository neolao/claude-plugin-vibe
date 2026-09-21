import functools


class ReportRepository:
    def __init__(self, data):
        self._data = data

    def fetch(self, report_id):
        return self._data.get(report_id)


class ReportFormatterService:
    def __init__(self, repository):
        self._repository = repository

    def format(self, report_id):
        report = self._repository.fetch(report_id)
        return f"Report #{report_id}: {report['title']}"


class ReportController:
    def __init__(self, formatter_service):
        self._formatter_service = formatter_service

    def handle(self, report_id):
        return self._formatter_service.format(report_id)


@functools.lru_cache(maxsize=1024)
def compute_title_word_count(title):
    return len(title.split())
