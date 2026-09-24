from address import Address


class Customer:
    def __init__(self, customer_id: str, name: str, address: Address):
        self.customer_id = customer_id
        self.name = name
        self.address = address

    def move_to(self, address: Address) -> None:
        self.address = address

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Customer) and other.customer_id == self.customer_id

    def __hash__(self) -> int:
        return hash(self.customer_id)
