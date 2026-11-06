"""Ticket priorities and the response time promised for each."""

PRIORITIES = ("low", "normal", "urgent")

SLA_HOURS = {
    "low": 72,
    "normal": 24,
    "urgent": 4,
}


def sla_hours(priority):
    return SLA_HOURS[priority]
