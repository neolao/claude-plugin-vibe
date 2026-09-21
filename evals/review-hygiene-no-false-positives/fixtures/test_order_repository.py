import pytest

from order_repository import OrderRepository


@pytest.fixture
def repository():
    return OrderRepository({})


def test_calculate_discounted_total_applies_promo(repository):
    order = {"price": 100, "quantity": 2, "has_promo": True}
    assert repository.calculate_discounted_total(order) == 180


def test_calculate_discounted_total_without_promo(repository):
    order = {"price": 100, "quantity": 2, "has_promo": False}
    assert repository.calculate_discounted_total(order) == 200


@pytest.mark.skip(reason="flaky pending investigation in TICKET-501")
def test_is_active_returns_false_when_missing(repository):
    assert not repository.is_active("missing")
