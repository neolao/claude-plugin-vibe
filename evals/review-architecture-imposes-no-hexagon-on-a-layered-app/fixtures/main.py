"""Application wiring."""

from controllers.orders_controller import OrdersController
from repositories.order_repository import OrderRepository
from services.order_service import OrderService


def build_controller() -> OrdersController:
    return OrdersController(OrderService(OrderRepository()))
