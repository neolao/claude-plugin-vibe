# Called from the account settings page when a customer edits their street.
from customer import Customer


def update_street(customer: Customer, street: str) -> None:
    customer.address.street = street
