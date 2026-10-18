# ledger

Python 3, standard library only. Tests: `python3 -m unittest -q` from the repo root, files `tests/test_*.py`.

## Conventions
- One export format = one subclass of `exports.base.Exporter`, registered in `exports/__init__.py`. The admin page only knows the registry.
- Money is handled in integer cents; formatting happens in the exporter.
