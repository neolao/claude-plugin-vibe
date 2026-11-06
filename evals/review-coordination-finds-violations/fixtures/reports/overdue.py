"""Daily overdue report sent to the team lead every morning."""
from datetime import datetime


def overdue_tickets(tickets, now=None):
    now = now or datetime.utcnow()
    return [t for t in tickets if t.status == "open" and t.due_at < now]


def render(tickets):
    lines = [f"{t.reference}\t{t.priority}\t{t.due_at:%Y-%m-%d}" for t in overdue_tickets(tickets)]
    return "\n".join(lines)
