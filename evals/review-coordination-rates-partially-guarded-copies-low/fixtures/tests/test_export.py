import unittest

from orders.status import STATUSES
from reports.export import STATUS_LABELS


class ExportLabelsTest(unittest.TestCase):
    def test_every_status_has_a_label(self):
        self.assertEqual(set(STATUS_LABELS), set(STATUSES))
