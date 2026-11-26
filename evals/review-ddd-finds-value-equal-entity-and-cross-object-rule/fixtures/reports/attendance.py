# Printed by the front desk each evening.
from dataclasses import dataclass


@dataclass(frozen=True)
class AttendanceLine:
    session_id: str
    member_name: str
    room: str


def attendance_lines(sessions) -> list[AttendanceLine]:
    lines = []
    for session in sessions:
        for member in session.attendees:
            lines.append(AttendanceLine(session.session_id, member.name, session.slot.room))
    return sorted(set(lines), key=lambda line: (line.session_id, line.member_name))
