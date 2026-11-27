from csv_exporter import CsvExporter
from export_settings import ExportSettings


def export_stock_levels(stock_rows, path):
    """Entry point of the nightly inventory export, streamed to the warehouse system."""
    exporter = CsvExporter(ExportSettings(chunk_size=5000, delimiter=","))
    with open(path, "w") as handle:
        exporter.write(stock_rows, handle)
