import unittest

from notifications.templates import SUBJECT_PREFIX, order_confirmed


class Order:
    reference = "A1B2"


class TemplatesTest(unittest.TestCase):
    def test_subject_prefix(self):
        self.assertEqual(SUBJECT_PREFIX, "[Shop] ")

    def test_confirmation_subject_carries_the_reference(self):
        self.assertEqual(order_confirmed(Order())["subject"], "[Shop] Order A1B2 confirmed")
