"""Labels printed on the pay slips."""


def pay_slip_label(employee, month):
    """Header line of a pay slip, e.g. 'Pay slip - Ada Lovelace - 2026-03'."""
    if not employee.strip():
        raise ValueError("employee name required")
    return f"Pay slip - {employee.strip()} - {month}"
