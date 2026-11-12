import unittest

from mail.parser import order_reference
from notifications.templates import order_confirmed


class Order:
    reference = "A1B2"


class ParserTest(unittest.TestCase):
    def test_reply_to_a_confirmation_gives_back_the_reference(self):
        subject = "Re: " + order_confirmed(Order())["subject"]
        self.assertEqual(order_reference(subject), "A1B2")
