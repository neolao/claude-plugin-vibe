class NotificationService:
    def __init__(self, channel, retry_count):
        self._channel = channel
        self._retry_count = retry_count

    def notify(self, recipient, message):
        last_error = None
        for _ in range(self._retry_count):
            try:
                self._channel.send(recipient, message)
                return
            except ConnectionError as error:
                last_error = error
        raise last_error
