# Called from the member app's profile page.
class UpdateContact:
    def __init__(self, members):
        self._members = members

    def execute(self, member_id: str, email: str) -> None:
        member = self._members.get(member_id)
        member.change_email(email)
        self._members.save(member)
