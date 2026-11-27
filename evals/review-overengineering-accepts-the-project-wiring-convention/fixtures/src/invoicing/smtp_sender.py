import smtplib


class SmtpSender:
    def __init__(self, host):
        self._smtp = smtplib.SMTP(host, 25)

    def send(self, recipient, body):
        self._smtp.sendmail("billing@example.com", recipient, body)
