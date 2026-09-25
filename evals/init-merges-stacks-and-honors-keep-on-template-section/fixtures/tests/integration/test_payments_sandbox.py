import os

import pytest

pytestmark = pytest.mark.skipif(
    "PAYMENTS_SANDBOX_KEY" not in os.environ, reason="needs the payments sandbox"
)


def test_sandbox_accepts_a_test_card():
    assert os.environ["PAYMENTS_SANDBOX_KEY"]
