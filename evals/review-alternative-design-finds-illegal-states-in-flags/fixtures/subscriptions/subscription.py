"""Customer subscription record. Loaded from and saved to the `subscriptions` table."""
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Subscription:
    id: int
    plan: str
    is_trial: bool = True
    is_active: bool = False
    is_paused: bool = False
    is_cancelled: bool = False
    trial_ends: Optional[date] = None
    paused_since: Optional[date] = None
    cancelled_on: Optional[date] = None

    def start_paid(self) -> None:
        self.is_trial = False
        self.is_active = True

    def pause(self, today: date) -> None:
        self.is_paused = True
        self.paused_since = today

    def resume(self) -> None:
        self.is_paused = False
        self.paused_since = None

    def cancel(self, today: date) -> None:
        self.is_cancelled = True
        self.cancelled_on = today

    def can_be_billed(self) -> bool:
        return self.is_active and not self.is_paused and not self.is_cancelled

    def can_access_product(self) -> bool:
        if self.is_cancelled:
            return False
        if self.is_trial:
            return self.trial_ends is not None
        return self.is_active

    def label(self) -> str:
        if self.is_cancelled:
            return "Cancelled"
        if self.is_paused:
            return "Paused"
        if self.is_trial:
            return "Trial"
        if self.is_active:
            return "Active"
        return "Unknown"
