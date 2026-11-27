from viewer import gpu


def object_under_cursor(cursor):
    """Reads the id of the object drawn under the cursor from the id buffer."""
    pixel = gpu.read_pixels(cursor.x, cursor.y, 1, 1)
    return int.from_bytes(pixel, "little")
