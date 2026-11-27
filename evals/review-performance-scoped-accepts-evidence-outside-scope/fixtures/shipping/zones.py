import csv
from pathlib import Path

# One row per postcode district (the part before the space), about 3 000 rows.
with open(Path(__file__).with_name("postcode_zones.csv"), newline="") as f:
    _DISTRICTS = [(row["district"], row["zone"]) for row in csv.DictReader(f)]

_PRICE_PER_KG_CENTS = {"A": 450, "B": 620, "C": 890, "D": 1250}


def zone_for(postcode):
    district = postcode.split()[0].upper()
    for known, zone in _DISTRICTS:
        if known == district:
            return zone
    raise ValueError(f"no shipping zone for postcode {postcode!r}")


def price_cents(postcode, weight_g):
    kilos = max(1, -(-weight_g // 1000))
    return _PRICE_PER_KG_CENTS[zone_for(postcode)] * kilos
