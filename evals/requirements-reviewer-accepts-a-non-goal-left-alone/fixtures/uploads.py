"""Upload storage. Called by the shop owner's photo form."""

import logging

log = logging.getLogger("uploads")

JPEG_QUALITY = 80


def compress(image):
    return {"name": image["name"], "size": image["size"] // 2, "quality": JPEG_QUALITY}


def store_upload(image, store):
    compressed = compress(image)
    store[compressed["name"]] = compressed
    log.info("stored %s: %d -> %d bytes", image["name"], image["size"], compressed["size"])
    return compressed
