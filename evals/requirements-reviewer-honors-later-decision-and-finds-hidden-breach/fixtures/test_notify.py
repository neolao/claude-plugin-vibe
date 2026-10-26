import unittest

from hooks import after_movement


class FakeMailer:
    def __init__(self):
        self.sent = []

    def send(self, to, subject, body):
        self.sent.append((to, subject, body))


class AfterMovementTest(unittest.TestCase):
    def test_sends_below_threshold(self):
        mailer = FakeMailer()
        product = {"name": "Bolt", "threshold": 10}
        self.assertTrue(after_movement(product, 4, mailer, "stock@example.com"))
        self.assertEqual(len(mailer.sent), 1)

    def test_silent_above_threshold(self):
        mailer = FakeMailer()
        product = {"name": "Bolt", "threshold": 10}
        self.assertFalse(after_movement(product, 12, mailer, "stock@example.com"))
        self.assertEqual(mailer.sent, [])


if __name__ == "__main__":
    unittest.main()
