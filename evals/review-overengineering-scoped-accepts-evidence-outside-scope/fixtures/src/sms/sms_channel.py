import urllib.request

from notifications.channel import NotificationChannel


class SmsChannel(NotificationChannel):
    def send(self, recipient, message):
        body = f"to={recipient}&text={message}".encode()
        with urllib.request.urlopen("https://sms.example.com/send", data=body, timeout=5) as response:
            if response.status >= 400:
                raise ConnectionError(f"sms gateway answered {response.status}")
