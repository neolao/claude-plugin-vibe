from money import Money


class ApprovalRequired(Exception):
    """Raised when closing an order needs a manager's approval."""


class OrderApprovalService:
    """Decides whether closing an order needs manager approval."""

    APPROVAL_THRESHOLD = Money(500, "EUR")

    def needs_approval(self, order, pricing):
        total = Money(0, self.APPROVAL_THRESHOLD.currency)
        for item in order.items:
            total = total.add(pricing[item.sku].times(item.qty))
        return total.exceeds(self.APPROVAL_THRESHOLD)


class CloseOrderUseCase:
    """Closes an order, asking for manager approval above the threshold."""

    def __init__(self, orders, pricing, approval_service):
        self._orders = orders
        self._pricing = pricing
        self._approval_service = approval_service

    def execute(self, order_id, approved_by_manager):
        order = self._orders.get(order_id)
        if self._approval_service.needs_approval(order, self._pricing) and not approved_by_manager:
            raise ApprovalRequired(order_id)
        order.close()
        self._orders.save(order)
