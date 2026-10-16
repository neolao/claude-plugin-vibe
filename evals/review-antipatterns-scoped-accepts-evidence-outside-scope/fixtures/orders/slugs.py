"""URL slugs for the public order-tracking page."""

import re
import unicodedata


def slugify(title):
    ascii_title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    words = re.findall(r"[a-z0-9]+", ascii_title.lower())
    return "-".join(words)
