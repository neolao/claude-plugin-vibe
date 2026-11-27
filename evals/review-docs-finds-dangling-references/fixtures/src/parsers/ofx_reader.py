"""OFX statement reader: one Transaction per STMTTRN record."""

from src.parsers.csv_reader import Transaction


def read(path):
    with open(path) as handle:
        for record in _records(handle.read()):
            yield Transaction(record["DTPOSTED"][:8], record["NAME"], float(record["TRNAMT"]), "EUR")


def _records(text):
    for chunk in text.split("<STMTTRN>")[1:]:
        body = chunk.split("</STMTTRN>")[0]
        yield dict(line.strip("<").split(">", 1) for line in body.strip().splitlines() if ">" in line)
