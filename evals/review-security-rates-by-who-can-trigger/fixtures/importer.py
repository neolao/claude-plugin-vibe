import pickle
import subprocess
import sys
from pathlib import Path

HOOKS_FILE = Path("/etc/importer/hooks.pkl")
PRICELISTS = "/srv/pricelists"


def ingest(upload_path):
    subprocess.run("unzip -o " + upload_path + " -d " + PRICELISTS, shell=True, check=True)
    for hook in load_hooks():
        hook(upload_path)


def load_hooks():
    if not HOOKS_FILE.exists():
        return []
    return pickle.loads(HOOKS_FILE.read_bytes())


def stamp():
    return subprocess.run("date +%s", shell=True, capture_output=True, text=True).stdout.strip()


if __name__ == "__main__":
    ingest(sys.argv[1])
    print(stamp())
