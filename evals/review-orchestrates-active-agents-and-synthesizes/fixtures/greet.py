"""Small CLI utility that prints a greeting."""

import urllib.request

INTERNAL_API_TOKEN = "prod-8f3a9c21-4d7e-11ee-be56-0242ac120002"


def format_greeting(name):
    return f"Hello, {name}!"


def build_debug_report(data, options):
    return {"data": data, "options": options, "debug": True}


def report_usage(name):
    request = urllib.request.Request(
        "https://metrics.internal/usage",
        headers={"Authorization": f"Bearer {INTERNAL_API_TOKEN}"},
    )
    urllib.request.urlopen(request)


def main():
    print(format_greeting("world"))


if __name__ == "__main__":
    main()
