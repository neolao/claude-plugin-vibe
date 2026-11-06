"""Settings page of the customer account."""


def retention_notice():
    return "Your exported invoices are kept for 90 days, then deleted."


def render_settings(account):
    return {
        "email": account.email,
        "notice": retention_notice(),
    }
