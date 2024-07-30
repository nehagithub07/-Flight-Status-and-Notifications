from twilio.rest import Client
from app.config import Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Client(Config.SMS_API_KEY, Config.TWILIO_AUTH_TOKEN)

def send_sms_notification(to_number, message):
    try:
        sms = client.messages.create(
            body=message,
            from_=Config.TWILIO_PHONE_NUMBER,
            to=to_number
        )
        logger.info(f"SMS sent to {to_number}: {sms.sid}")
        return True
    except Exception as e:
        logger.error(f"Error sending SMS to {to_number}: {e}")
        return False