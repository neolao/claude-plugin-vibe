from pricing.money import Money


class Product:
    def __init__(self, sku: str, name: str, price: Money):
        self.sku = sku
        self.name = name
        self.price = price

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Product) and other.sku == self.sku

    def __hash__(self) -> int:
        return hash(self.sku)


# Loaded once at startup from the catalog file; shared by every basket.
CATALOG: dict[str, Product] = {}
