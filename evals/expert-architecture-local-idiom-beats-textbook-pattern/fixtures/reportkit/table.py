from dataclasses import dataclass


@dataclass(frozen=True)
class Table:
    columns: list[str]
    rows: list[list[str]]
