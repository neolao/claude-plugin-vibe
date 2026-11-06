import unittest

from tickets.limits import MAX_ATTACHMENTS, check_attachments


class Ticket:
    def __init__(self, count):
        self.reference = "T-9"
        self.attachments = list(range(count))


class LimitsTest(unittest.TestCase):
    def test_limit_value(self):
        self.assertEqual(MAX_ATTACHMENTS, 5)

    def test_sixth_attachment_is_refused(self):
        with self.assertRaises(ValueError):
            check_attachments(Ticket(6))
