"""Counters of placed orders, read by the health endpoint."""


class Collector:
    def __init__(self) -> None:
        self._orders = 0
        self._cents = 0

    def record(self, total_cents: int) -> None:
        self._orders += 1
        self._cents += total_cents

    def snapshot(self) -> dict[str, int]:
        return {"orders": self._orders, "cents": self._cents}
