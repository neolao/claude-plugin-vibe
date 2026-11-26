from studio.member import Member
from studio.slot import Slot


class AlreadyEnrolled(Exception):
    pass


class SessionFull(Exception):
    pass


class ClassSession:
    def __init__(self, session_id: str, slot: Slot, capacity: int):
        self.session_id = session_id
        self.slot = slot
        self.capacity = capacity
        self._attendees: list[Member] = []

    def enrol(self, member: Member) -> None:
        if member in self._attendees:
            raise AlreadyEnrolled(member.member_id)
        if len(self._attendees) >= self.capacity:
            raise SessionFull(self.session_id)
        self._attendees.append(member)

    def withdraw(self, member: Member) -> None:
        self._attendees.remove(member)

    @property
    def attendees(self) -> tuple[Member, ...]:
        return tuple(self._attendees)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ClassSession) and other.session_id == self.session_id

    def __hash__(self) -> int:
        return hash(self.session_id)
