from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    """Extension point for notification channels."""

    @abstractmethod
    def send(self, message):
        raise NotImplementedError


class EmailChannel(NotificationChannel):
    def send(self, message):
        print(f"sending email: {message}")


class NotificationChannelFactory:
    """Builds the notification channel to use."""

    def create(self):
        return EmailChannel()


class NotificationService:
    def __init__(self, retry_count):
        self.retry_count = retry_count
        self.channel = NotificationChannelFactory().create()

    def notify(self, message):
        for _ in range(self.retry_count):
            self.channel.send(message)
            return


def send_welcome_email(user):
    NotificationService(retry_count=3).notify(f"Welcome {user}")


def send_password_reset_email(user):
    NotificationService(retry_count=3).notify(f"Reset your password, {user}")
