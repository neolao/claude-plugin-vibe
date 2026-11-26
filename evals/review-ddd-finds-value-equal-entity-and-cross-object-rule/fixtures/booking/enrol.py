# Called from the member app when a member books a place in a class.
class EnrolInSession:
    def __init__(self, members, sessions):
        self._members = members
        self._sessions = sessions

    def execute(self, member_id: str, session_id: str) -> None:
        member = self._members.get(member_id)
        session = self._sessions.get(session_id)
        session.enrol(member)
        self._sessions.save(session)
