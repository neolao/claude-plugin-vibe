"""Small CLI utility that prints a greeting."""

# Committed by mistake alongside real config — looks exactly like a live credential.
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def format_greeting(name):
    return f"Hello, {name}!"


def build_debug_report(data, options):
    # Not called anywhere in this codebase.
    return {"data": data, "options": options, "debug": True}


def main():
    print(format_greeting("world"))


if __name__ == "__main__":
    main()
