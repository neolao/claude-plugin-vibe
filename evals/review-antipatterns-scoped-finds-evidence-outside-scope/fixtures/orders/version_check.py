"""Compatibility check on the version the mobile client sends in its headers."""

MIN_CLIENT_VERSION = "4.12.0"


def parse_version(text):
    major, minor, patch = text.split(".")
    return int(major), int(minor), int(patch)


def client_supported(header_value):
    return parse_version(header_value) >= parse_version(MIN_CLIENT_VERSION)
