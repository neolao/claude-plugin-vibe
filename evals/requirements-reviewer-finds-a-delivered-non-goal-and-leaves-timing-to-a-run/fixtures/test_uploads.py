import unittest

from uploads import store_upload

IMAGE = {"name": "shop-front.jpg", "size": 4_000_000, "quality": 100}


class StoreUploadTest(unittest.TestCase):
    def test_stores_the_image_compressed(self):
        store = {}
        stored = store_upload(IMAGE, store)
        self.assertEqual(stored["quality"], 80)
        self.assertEqual(stored["name"], "shop-front.jpg")
        self.assertLess(stored["size"], IMAGE["size"])
        self.assertIs(store["shop-front.jpg"], stored)

    def test_logs_both_sizes(self):
        with self.assertLogs("uploads", level="INFO") as logs:
            store_upload(IMAGE, {})
        self.assertEqual(logs.output, ["INFO:uploads:stored shop-front.jpg: 4000000 -> 2000000 bytes"])


if __name__ == "__main__":
    unittest.main()
