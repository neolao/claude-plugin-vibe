class CsvExporter:
    def __init__(self, settings):
        self._settings = settings

    def write(self, rows, handle):
        chunk = []
        for row in rows:
            chunk.append(self._settings.delimiter.join(str(value) for value in row))
            if len(chunk) == self._settings.chunk_size:
                handle.write("\n".join(chunk) + "\n")
                chunk = []
        if chunk:
            handle.write("\n".join(chunk) + "\n")
