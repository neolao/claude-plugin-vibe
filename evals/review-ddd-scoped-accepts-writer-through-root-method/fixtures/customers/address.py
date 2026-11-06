from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Address:
    street: str
    city: str
    postcode: str

    def with_street(self, street: str) -> "Address":
        return replace(self, street=street)
