from dataclasses import dataclass


@dataclass
class Member:
    member_id: str
    name: str
    email: str
    tier: str

    def change_email(self, email: str) -> None:
        if "@" not in email:
            raise ValueError("invalid email")
        self.email = email
