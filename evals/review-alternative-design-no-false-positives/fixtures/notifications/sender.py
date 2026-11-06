import smtplib
import urllib.request


SMS_GATEWAY_URL = "https://sms.example.com/send"


def send(message):
    """Called once per order event with the channel the customer chose at signup."""
    if message["channel"] == "email":
        with smtplib.SMTP("localhost") as smtp:
            smtp.sendmail("shop@example.com", message["to"], message["body"])
    elif message["channel"] == "sms":
        data = f"to={message['to']}&body={message['body']}".encode()
        with urllib.request.urlopen(SMS_GATEWAY_URL, data=data, timeout=5) as response:
            response.read()
    else:
        raise ValueError(f"unknown channel: {message['channel']}")
