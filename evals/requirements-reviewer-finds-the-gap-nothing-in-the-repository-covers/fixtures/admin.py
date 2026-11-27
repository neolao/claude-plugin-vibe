"""Admin page. Lists every coupon with its code, discount and expiry date."""


def coupon_rows(coupons):
    return [
        {"code": c["code"], "discount": c["discount"], "expires": c["expires"].isoformat()}
        for c in coupons
    ]
