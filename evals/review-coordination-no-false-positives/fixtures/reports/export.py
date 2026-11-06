"""Daily CSV export of every ticket, read by the team lead's spreadsheet."""
import csv

from tickets.status_names import STATUS_NAMES

COLUMNS = ("reference", "status", "priority")


def export_tickets(tickets, path):
    with open(path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(COLUMNS)
        for ticket in tickets:
            writer.writerow([ticket.reference, STATUS_NAMES[ticket.status], ticket.priority])
