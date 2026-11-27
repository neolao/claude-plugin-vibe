import csv


class CsvExporter:
    def write(self, rows, path):
        with open(path, "w", newline="") as handle:
            writer = csv.writer(handle)
            for row in rows:
                writer.writerow(row)
