import os
import tempfile
import unittest

from parser import read_contacts


class ReadContactsTest(unittest.TestCase):
    def test_reads_one_line_per_contact(self):
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
            f.write("ada,ada@example.com\nlin,lin@example.com\n")
        try:
            self.assertEqual(len(read_contacts(f.name)), 2)
        finally:
            os.unlink(f.name)

    def test_empty_file_is_refused(self):
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
            pass
        try:
            with self.assertRaises(ValueError):
                read_contacts(f.name)
        finally:
            os.unlink(f.name)


if __name__ == "__main__":
    unittest.main()
