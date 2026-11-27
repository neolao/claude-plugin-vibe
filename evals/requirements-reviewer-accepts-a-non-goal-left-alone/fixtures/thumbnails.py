"""Gallery thumbnails. Rendered on the shop's gallery page."""

THUMB_WIDTH = 120


def thumbnail(image):
    return {"name": image["name"], "width": THUMB_WIDTH}
