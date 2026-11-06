# Builds the monthly statement line from the payment gateway's CSV export.
from dataclasses import dataclass


@dataclass
class GatewayPayment:
    """One row of the gateway's export, with the gateway's own column names."""

    reference: str
    gross_cents: int
    fee_cents: int
    currency: str


@dataclass
class InvoiceSummary:
    reference: str
    net_cents: int
    currency: str


def summarize(payment: GatewayPayment) -> InvoiceSummary:
    net = payment.gross_cents - payment.fee_cents
    return InvoiceSummary(payment.reference, net, payment.currency)
