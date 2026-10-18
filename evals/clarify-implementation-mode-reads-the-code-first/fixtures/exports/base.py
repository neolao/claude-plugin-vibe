"""Export formats of the monthly report. Called from the admin page through the registry."""


class Exporter:
    extension = ""

    def render(self, rows):
        """Return the file body as bytes. `rows` are dicts with date, amount_cents, label."""
        raise NotImplementedError

    def file_name(self, month):
        return f"report-{month}.{self.extension}"
