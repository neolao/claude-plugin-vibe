import unittest
from unittest import mock

from shop.dispatch import dispatch


class DispatchTests(unittest.TestCase):
    def setUp(self):
        self.order = mock.Mock()

    def test_billing_marks_the_order_paid(self):
        dispatch("billing", self.order)
        self.order.mark_paid.assert_called_once_with()

    def test_shipping_marks_the_order_shipped(self):
        dispatch("shipping", self.order)
        self.order.mark_shipped.assert_called_once_with()
