"""Pricing rules per customer tier: line amounts, rebate, VAT once at the end."""

from typing import Protocol

VAT_PERCENT = 20


class PricingPolicy(Protocol):
    def total(self, line_amounts_cents: list[int]) -> int: ...


class StandardPricing:
    def total(self, line_amounts_cents: list[int]) -> int:
        subtotal = sum(line_amounts_cents)
        return subtotal + subtotal * VAT_PERCENT // 100


class WholesalePricing:
    REBATE_PERCENT = 8

    def total(self, line_amounts_cents: list[int]) -> int:
        subtotal = sum(line_amounts_cents)
        subtotal -= subtotal * self.REBATE_PERCENT // 100
        return subtotal + subtotal * VAT_PERCENT // 100


def policy_for(customer_tier: str) -> PricingPolicy:
    return WholesalePricing() if customer_tier == "wholesale" else StandardPricing()
