class PdfRenderer:
    def __init__(self):
        self._lines = []

    def render(self, title, lines):
        self._lines = [title, *lines]
        return "\n".join(self._lines).encode()
