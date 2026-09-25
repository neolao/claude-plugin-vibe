import pytest
from freezegun import freeze_time

from report_builder.render import render_report


@pytest.fixture
def signing_key(monkeypatch):
    monkeypatch.setenv("REPORT_SIGNING_KEY", "test-key")


@freeze_time("2026-01-01")
def test_render_report_writes_the_issue_date(signing_key):
    report = render_report({"issued_at": "2026-03-04T10:00:00", "template": "<p><time></time></p>"})
    assert "2026-03-04" in report["html"]
