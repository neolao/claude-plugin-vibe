import unittest

import config


class ConfigTest(unittest.TestCase):
    def test_port_is_an_int(self):
        self.assertIsInstance(config.PORT, int)

    def test_retries_are_bounded(self):
        self.assertLessEqual(config.RETRIES, 5)


if __name__ == "__main__":
    unittest.main()
