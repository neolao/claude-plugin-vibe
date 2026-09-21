# CLAUDE.md — tiny-lib

## Project overview

`tiny-lib` is a small standalone Python utility library (`listutils.py`), dependency-free, with no packaging manifest.

## Testing conventions

Run the test suite with:

    python3 -m unittest discover -s . -p "test_*.py" -v

Lint: `python3 -m py_compile listutils.py test_listutils.py` (no dedicated linter configured).

No run or dev command: this is a library, not a service — there is nothing to start.

## Constraints

- Keep the library dependency-free (standard library only).
- Do not add a packaging manifest (`pyproject.toml`, `setup.py`) without an explicit request.
