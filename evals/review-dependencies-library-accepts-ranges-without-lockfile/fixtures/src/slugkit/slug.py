import re

from dateutil import parser as date_parser
from unidecode import unidecode

_NON_WORD = re.compile(r"[^a-z0-9]+")


def slugify(title: str, dated: str | None = None) -> str:
    """Lower-case ASCII words joined by dashes, optionally prefixed by an ISO date."""
    ascii_title = unidecode(title).lower()
    slug = _NON_WORD.sub("-", ascii_title).strip("-")
    if dated is None:
        return slug
    day = date_parser.parse(dated).date()
    return f"{day.isoformat()}-{slug}"
