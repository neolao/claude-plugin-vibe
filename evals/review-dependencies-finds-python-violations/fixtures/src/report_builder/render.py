"""Fills a partner's HTML template with the report's issue date."""
from bs4 import BeautifulSoup
from dateutil import parser as date_parser

from .signing import sign


def render_report(spec):
    issued = date_parser.isoparse(spec["issued_at"])
    soup = BeautifulSoup(spec["template"], "html.parser")
    soup.find("time").string = issued.strftime("%Y-%m-%d")
    html = str(soup)
    return {"html": html, "signature": sign(html)}
