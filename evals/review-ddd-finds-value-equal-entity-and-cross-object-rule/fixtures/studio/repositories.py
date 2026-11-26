from studio.member import Member
from studio.session import ClassSession


class MemberRepository:
    def __init__(self, rows: dict[str, dict]):
        self._rows = rows

    def get(self, member_id: str) -> Member:
        row = self._rows[member_id]
        return Member(row["id"], row["name"], row["email"], row["tier"])

    def save(self, member: Member) -> None:
        self._rows[member.member_id] = {
            "id": member.member_id,
            "name": member.name,
            "email": member.email,
            "tier": member.tier,
        }


class SessionRepository:
    def __init__(self):
        self._sessions: dict[str, ClassSession] = {}

    def get(self, session_id: str) -> ClassSession:
        return self._sessions[session_id]

    def save(self, session: ClassSession) -> None:
        self._sessions[session.session_id] = session
