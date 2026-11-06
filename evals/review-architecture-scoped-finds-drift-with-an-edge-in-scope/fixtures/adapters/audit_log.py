"""Driven adapter: appends one line per audited action to the audit file."""

from datetime import datetime, timezone

from adapters.config import AUDIT_PATH


class AuditLog:
    def record(self, line: str) -> None:
        stamp = datetime.now(timezone.utc).isoformat()
        with open(AUDIT_PATH, "a", encoding="utf-8") as audit:
            audit.write(f"{stamp} {line}\n")
