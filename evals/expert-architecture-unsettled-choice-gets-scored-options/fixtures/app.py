"""Composition root. Called once at process start; serves POST /notifications."""

from adapters.notify.email import EmailNotifier
from adapters.notify.push import PushNotifier
from core.notification_service import NotificationService

service = NotificationService(email=EmailNotifier.from_env(), push=PushNotifier.from_env())


def post_notification(payload):
    return service.send(payload.to_message())
