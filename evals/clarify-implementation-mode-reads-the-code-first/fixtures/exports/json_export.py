import json

from exports.base import Exporter


class JsonExporter(Exporter):
    extension = "json"

    def render(self, rows):
        return json.dumps(rows, indent=2).encode("utf-8")
