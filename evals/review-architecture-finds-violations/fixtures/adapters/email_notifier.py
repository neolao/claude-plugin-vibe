from core.email_templates import render_receipt_html


class EmailNotifier:
    def send(self, order):
        body = render_receipt_html(order)
        print(f"emailing receipt for order {order.get('id')} ({len(body)} bytes)")
