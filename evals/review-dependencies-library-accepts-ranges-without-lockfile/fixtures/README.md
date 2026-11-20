# slugkit

Turns titles into URL slugs, with transliteration of accented letters and an
optional date prefix. Published on PyPI:

```
pip install slugkit
```

```python
from slugkit import slugify

slugify("Café au lait")                       # "cafe-au-lait"
slugify("Café au lait", dated="2026-03-04")   # "2026-03-04-cafe-au-lait"
```

Supports Python 3.10 and later. Run the tests with `pytest`.
