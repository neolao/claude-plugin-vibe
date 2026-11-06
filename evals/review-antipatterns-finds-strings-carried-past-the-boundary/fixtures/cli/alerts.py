"""Export notifications."""


def notify(environment, row_count):
    if environment == "production" or environment == "staging":
        print(f"[{environment}] exported {row_count} rows")
