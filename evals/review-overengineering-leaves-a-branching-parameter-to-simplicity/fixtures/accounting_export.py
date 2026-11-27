from csv_exporter import CsvExporter
from export_settings import ExportSettings


def export_ledger(ledger_rows, path):
    """Entry point of the monthly accounting export, read by the accountant's spreadsheet."""
    exporter = CsvExporter(ExportSettings(chunk_size=500, delimiter=";"))
    with open(path, "w") as handle:
        exporter.write(ledger_rows, handle)
