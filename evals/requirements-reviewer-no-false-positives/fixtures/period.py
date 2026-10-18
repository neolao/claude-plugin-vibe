"""Period filter of the monthly report. Called from the admin page."""


def _in_period(date, start, end):
    return start <= date <= end


def filter_period(rows, start, end):
    if start > end:
        raise ValueError("start must not follow end")
    return [row for row in rows if _in_period(row["date"], start, end)]
