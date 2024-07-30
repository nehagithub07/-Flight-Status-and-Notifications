import pika
from app.config import Config
from app.notification_service.sms_service import send_sms_notification
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def on_message(channel, method, properties, body):
    try:
        message_content = json.loads(body.decode('utf-8'))
        to_number = message_content.get('to')
        message = message_content.get('message')
        
        if to_number and message:
            send_sms_notification(to_number, message)
            logger.info(f"Notification sent to {to_number}")
        else:
            logger.error("Invalid message format")
        
        channel.basic_ack(delivery_tag=method.delivery_tag)
    except json.JSONDecodeError:
        logger.error("Failed to decode message")
    except Exception as e:
        logger.error(f"Error processing message: {e}")

def start_rabbitmq_consumer():
    try:
        connection = pika.BlockingConnection(pika.URLParameters(Config.RABBITMQ_URL))
        channel = connection.channel()
        channel.queue_declare(queue='flight_notifications')

        channel.basic_consume(queue='flight_notifications', on_message_callback=on_message)

        logger.info("Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()
    except pika.exceptions.AMQPConnectionError:
        logger.error("Failed to connect to RabbitMQ")
    except KeyboardInterrupt:
        logger.info("Interrupted")
    finally:
        if connection.is_open:
            connection.close()