from notifier import mail


def test_sends_confirmation(postal):
    response = mail.send(
        to="qa@shop.example", subject="Order 42", body="Thanks", api_key=postal["api_key"], url=postal["url"]
    )
    assert response.status == 200
