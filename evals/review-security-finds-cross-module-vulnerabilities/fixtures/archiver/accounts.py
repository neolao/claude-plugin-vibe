import os
import pwd
from dataclasses import dataclass
from pathlib import Path

ROLES_FILE = Path("/etc/archiver/roles")


@dataclass(frozen=True)
class User:
    name: str
    role: str


def current():
    name = pwd.getpwuid(os.getuid()).pw_name
    return User(name=name, role=_roles().get(name, "viewer"))


def _roles():
    roles = {}
    for line in ROLES_FILE.read_text().splitlines():
        name, _, role = line.partition(":")
        roles[name.strip()] = role.strip()
    return roles
