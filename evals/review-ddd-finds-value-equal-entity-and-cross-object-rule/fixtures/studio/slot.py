from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Slot:
    starts_at: datetime
    room: str
