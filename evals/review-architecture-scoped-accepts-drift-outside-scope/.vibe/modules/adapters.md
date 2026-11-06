# Module: adapters

**Role:** Driven adapters implementing core's ports: the Postgres gateway and the
SMTP notifier.
**Files:** `adapters/postgres_gateway.py`, `adapters/smtp_notifier.py`, `adapters/config.py`
**Exports:** `PostgresGateway`, `SmtpNotifier`
**Depends on:** [`modules/core.md`](core.md) (implements `OrderGatewayPort` and `NotifierPort`)
