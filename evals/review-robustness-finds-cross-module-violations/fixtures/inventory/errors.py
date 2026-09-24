class SupplierError(Exception):
    def __init__(self, sku):
        super().__init__(f"supplier stock lookup failed for {sku}")
        self.sku = sku


class SyncFailed(Exception):
    def __init__(self, cause):
        super().__init__("inventory sync failed")
