from pathlib import Path

import yaml

from notifier import mail

ACCOUNT = yaml.safe_load(Path(__file__).with_name("fixtures").joinpath("postal_account.yaml").read_text())


def test_sends_confirmation():
    response = mail.send(ACCOUNT["api_key"], to="qa@shop.example", subject="Order 42", body="Thanks")
    assert response.status == 200
