import csv

from plugins.registry import register


@register("csv")
class CsvImport:
    def rows(self, handle):
        return list(csv.reader(handle))
