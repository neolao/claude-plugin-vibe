from enum import Enum


class Environment(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class OutputFormat(Enum):
    TEXT = "text"
    JSON = "json"
