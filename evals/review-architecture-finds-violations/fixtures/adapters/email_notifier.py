class EmailNotifier:
    def send(self, order):
        print(f"emailing receipt for order {order.get('id')}")
