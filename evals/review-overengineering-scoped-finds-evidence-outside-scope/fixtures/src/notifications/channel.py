from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient, message):
        raise NotImplementedError


class EmailChannel(NotificationChannel):
    def send(self, recipient, message):
        print(f"email to {recipient}: {message}")
