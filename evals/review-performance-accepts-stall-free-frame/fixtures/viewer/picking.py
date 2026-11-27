from viewer import gpu


class Picker:
    """Hover picking with a one-frame delay: the readback requested during one
    frame is collected at the start of the next."""

    def __init__(self):
        self._pending = None
        self.hovered = None

    def collect(self):
        if self._pending is None:
            return
        pixel = gpu.read_if_ready(self._pending)
        if pixel is not None:
            self.hovered = int.from_bytes(pixel, "little")
            self._pending = None

    def request(self, cursor):
        if self._pending is None:
            self._pending = gpu.request_read_pixels(cursor.x, cursor.y, 1, 1)
