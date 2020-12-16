from twilio.rest import Client

from django.conf import settings
from django.utils import timezone

from ..utils import check_and_update_retry_attempts


def send_notification(notification):
    """
    Send Twilio notifications to the target device using the Twilio Client.

    Args:
        notification (Notification): The email notification to be sent.

    Returns:
        String: Whether the SMS has successfully sent, or an error message.
    """
    try:
        twilio_account_sid = settings.TWILIO_ACCOUNT_SID
        twilio_auth_token = settings.TWILIO_AUTH_TOKEN

        twilio_sender = settings.TWILIO_SENDER
        twilio_receiver = notification.target_user_record.target_user_id

        client = Client(twilio_account_sid, twilio_auth_token)

        client.messages.create(
            body=notification.body,
            from_=twilio_sender,
            to=twilio_receiver)

    except Exception as e:
        check_and_update_retry_attempts(notification)
        return ("{}: {}".format(type(e), e))

    else:
        notification.status = notification.DELIVERED
        notification.attempted_delivery = timezone.now()
        notification.save()
        return('SMS Successfully sent!')
