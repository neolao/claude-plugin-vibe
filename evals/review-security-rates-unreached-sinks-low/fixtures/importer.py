import pickle
import subprocess
import sys
from datetime import datetime
from pathlib import Path

CACHE_FILE = Path("/var/cache/importer/last.pkl")
PRICELISTS = "/srv/pricelists"
UPLOADS = "/srv/uploads"


def ingest(day):
    datetime.strptime(day, "%Y-%m-%d")
    subprocess.run("unzip -o " + UPLOADS + "/" + day + ".zip -d " + PRICELISTS, shell=True, check=True)
    prices = parse(Path(PRICELISTS, day + ".csv"))
    changed = {sku: price for sku, price in prices.items() if load_cache().get(sku) != price}
    save_cache(prices)
    return changed


def parse(path):
    prices = {}
    for line in path.read_text().splitlines():
        sku, _, price = line.partition(",")
        prices[sku] = price
    return prices


def load_cache():
    if not CACHE_FILE.exists():
        return {}
    return pickle.loads(CACHE_FILE.read_bytes())


def save_cache(prices):
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_bytes(pickle.dumps(prices))


def stamp():
    return subprocess.run("date +%s", shell=True, capture_output=True, text=True).stdout.strip()


if __name__ == "__main__":
    print(len(ingest(sys.argv[1])), "prices changed")
    print(stamp())
