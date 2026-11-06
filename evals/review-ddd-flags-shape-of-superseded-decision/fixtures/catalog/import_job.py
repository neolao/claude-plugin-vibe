# Called by the nightly job that loads the supplier's variant feed.
import csv
from pathlib import Path

from sqlalchemy.orm import Session

from catalog.models import Product, Variant


def import_variants(session: Session, feed: Path) -> int:
    added = 0
    with feed.open() as f:
        for row in csv.DictReader(f):
            product = session.get(Product, row["product_id"])
            if product is None:
                continue
            product.variants.append(Variant(sku=row["sku"], size=row["size"], product=product))
            added += 1
    session.commit()
    return added
