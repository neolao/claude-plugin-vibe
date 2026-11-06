"""Ticket statuses and the transitions the agents may apply."""

STATUSES = ("open", "waiting", "resolved", "closed")

TRANSITIONS = {
    "open": ("waiting", "resolved"),
    "waiting": ("open", "resolved"),
    "resolved": ("closed", "open"),
    "closed": (),
}


def can_move(current, target):
    return target in TRANSITIONS[current]
