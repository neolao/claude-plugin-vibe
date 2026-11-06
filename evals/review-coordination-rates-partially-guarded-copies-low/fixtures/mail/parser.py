"""Reads the replies customers send to the notification e-mails."""
import re

REFERENCE = re.compile(r"Order (\w+) ")


def order_reference(subject):
    cleaned = subject
    for marker in ("Re: ", "RE: ", "Fwd: "):
        cleaned = cleaned.replace(marker, "")
    if cleaned.startswith("[Shop] "):
        cleaned = cleaned[len("[Shop] "):]
    match = REFERENCE.match(cleaned)
    return match.group(1) if match else None
