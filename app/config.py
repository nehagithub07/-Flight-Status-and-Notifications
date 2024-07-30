import os

class Config:
    # RabbitMQ configuration
    RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672/')

    # MongoDB configuration
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
    
    # Twilio configuration
    SMS_API_KEY = os.getenv('SMS_API_KEY', 'TWILIO_KEY')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', 'AUTH_KEY')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', 'TWILI_NO')
    
    # Flight data URL
    FLIGHT_DATA_URL = os.getenv('FLIGHT_DATA_URL', 'C:/Users/nehas/Desktop/Flight Status and Notifications/data/flights.json')

    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    DEBUG = os.getenv('DEBUG', False)