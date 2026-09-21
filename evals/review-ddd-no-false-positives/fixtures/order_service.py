class OrderApprovalService:
    """Domain service: decides whether closing an order needs manager approval."""

    APPROVAL_THRESHOLD = 500

    def needs_approval(self, order, pricing):
        total = sum(item["qty"] * pricing[item["sku"]] for item in order.items)
        return total > self.APPROVAL_THRESHOLD


class CloseOrderUseCase:
    """Application use case: orchestrates the domain service and the repository."""

    def __init__(self, orders, pricing, approval_service):
        self._orders = orders
        self._pricing = pricing
        self._approval_service = approval_service

    def execute(self, order_id, approved_by_manager):
        order = self._orders.get(order_id)
        if self._approval_service.needs_approval(order, self._pricing) and not approved_by_manager:
            raise PermissionError("closing this order needs manager approval")
        order.close()
        self._orders.save(order)
