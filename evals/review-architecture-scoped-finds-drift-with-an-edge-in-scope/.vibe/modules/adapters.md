# Module: adapters

**Role:** Driven adapters implementing core's ports: the Postgres gateway, the
SMTP notifier and the audit log file.
**Files:** `adapters/postgres_gateway.py`, `adapters/smtp_notifier.py`, `adapters/audit_log.py`, `adapters/config.py`
**Exports:** `PostgresGateway`, `SmtpNotifier`, `AuditLog`
**Depends on:** [`modules/core.md`](core.md) (implements `OrderGatewayPort` and `NotifierPort`)
