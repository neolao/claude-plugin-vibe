import unittest
from datetime import date

from coupons import CouponError, apply_coupon

COUPON = {"code": "SPRING", "discount": 0.1, "expires": date(2026, 3, 31)}


class ApplyCouponTest(unittest.TestCase):
    def test_valid_coupon_lowers_the_total(self):
        cart = apply_coupon({"total": 50.0}, COUPON, today=date(2026, 3, 10))
        self.assertEqual(cart["total"], 45.0)

    def test_expired_coupon_is_refused(self):
        with self.assertRaises(CouponError) as refused:
            apply_coupon({"total": 50.0}, COUPON, today=date(2026, 4, 1))
        self.assertEqual(str(refused.exception), "Coupon expired")


if __name__ == "__main__":
    unittest.main()
