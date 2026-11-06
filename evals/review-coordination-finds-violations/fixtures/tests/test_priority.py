import unittest

from tickets.priority import PRIORITIES, SLA_HOURS


class PriorityTest(unittest.TestCase):
    def test_every_priority_has_an_sla(self):
        self.assertEqual(set(SLA_HOURS), set(PRIORITIES))
