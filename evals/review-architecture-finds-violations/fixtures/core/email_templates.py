import smtplib


def render_receipt_html(order):
    """Builds the HTML body of the receipt email."""
    return f"<html><body><h1>Receipt {order['id']}</h1></body></html>"


def send_receipt(order, host="smtp.internal"):
    with smtplib.SMTP(host) as server:
        server.sendmail("noreply@shop", order["email"], render_receipt_html(order))
