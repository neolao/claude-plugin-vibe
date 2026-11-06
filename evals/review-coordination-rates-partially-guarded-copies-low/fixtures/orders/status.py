"""Order statuses and the transitions the checkout and the back office may apply."""

STATUSES = ("pending", "paid", "shipped", "cancelled")

TRANSITIONS = {
    "pending": ("paid", "cancelled"),
    "paid": ("shipped", "cancelled"),
    "shipped": (),
    "cancelled": (),
}


def can_move(current, target):
    return target in TRANSITIONS[current]


class Order:
    def __init__(self, reference, status="pending"):
        self.reference = reference
        self.status = status

    def move_to(self, target):
        if not can_move(self.status, target):
            raise ValueError(f"{self.reference}: {self.status} -> {target} is not allowed")
        self.status = target
