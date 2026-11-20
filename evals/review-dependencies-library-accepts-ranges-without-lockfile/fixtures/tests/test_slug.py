import pytest

from slugkit import slugify


def test_transliterates_accents():
    assert slugify("Café au lait") == "cafe-au-lait"


def test_collapses_punctuation():
    assert slugify("Hello, world!!") == "hello-world"


def test_prefixes_the_date():
    assert slugify("Release notes", dated="4 March 2026") == "2026-03-04-release-notes"


def test_rejects_an_unparseable_date():
    with pytest.raises(ValueError):
        slugify("Release notes", dated="someday")
