# inventory

Python 3, standard library only. Tests: `python3 -m unittest -q` from the repo root; files `tests/test_*.py`, `unittest` style.

## Conventions
- Explicit names, no abbreviations.
- One function does one thing.
- Quantities are integers; a function that receives a bad quantity raises `ValueError` with a clear message.
