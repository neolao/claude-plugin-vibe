"""HTTP handlers for the order API."""

from core.order_service import OrderService
from core.reporting import monthly_totals


def handle_place_order(request):
    return {"total": OrderService().place_order(request["order"])}


def handle_monthly_report(request):
    return {"revenue": monthly_totals(request["month"])}
