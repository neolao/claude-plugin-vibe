import unittest
from unittest import mock

from sync import push_all


class PushAllTest(unittest.TestCase):
    def test_returns_ids_of_sent_records(self):
        send = mock.Mock()
        self.assertEqual(push_all([{"id": 1}, {"id": 2}], send), [1, 2])

    def test_retries_after_a_connection_error(self):
        send = mock.Mock(side_effect=[ConnectionError(), None])
        with mock.patch("sync.time.sleep"):
            self.assertEqual(push_all([{"id": 7}], send), [7])


if __name__ == "__main__":
    unittest.main()
