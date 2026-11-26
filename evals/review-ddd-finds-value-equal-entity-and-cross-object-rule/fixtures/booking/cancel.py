# Called from the member app when a member cancels a booked class.
class CancelBooking:
    def __init__(self, members, sessions, ledger, clock):
        self._members = members
        self._sessions = sessions
        self._ledger = ledger
        self._clock = clock

    def execute(self, member_id: str, session_id: str) -> None:
        member = self._members.get(member_id)
        session = self._sessions.get(session_id)

        hours_left = (session.slot.starts_at - self._clock.now()).total_seconds() / 3600
        fee_cents = 0
        if hours_left < 12 and member.tier != "premium":
            if hours_left < 2:
                fee_cents = 1000
            else:
                fee_cents = 500

        session.withdraw(member)
        self._sessions.save(session)
        if fee_cents:
            self._ledger.charge(member.member_id, fee_cents, "late cancellation")
