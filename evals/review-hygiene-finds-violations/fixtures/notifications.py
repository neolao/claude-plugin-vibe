class MailClient:
    def send(self, user, message):
        pass


def send_notification(user, message):
    print(f"DEBUG: sending to {user}: {message}")
    # old_client = LegacyMailer()
    # old_client.connect()
    # old_client.send(user, message)
    client = MailClient()
    client.send(user, message)
