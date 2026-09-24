# Called when a customer joins an existing household account, so that the
# whole household receives deliveries at the head's address.
from customer import Customer


class Household:
    def __init__(self, household_id: str, head: Customer):
        self.household_id = household_id
        self.head = head
        self._members = [head]

    def add_member(self, customer: Customer) -> None:
        customer.move_to(self.head.address)
        self._members.append(customer)

    @property
    def members(self) -> tuple[Customer, ...]:
        return tuple(self._members)
