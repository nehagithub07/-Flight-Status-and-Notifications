# Flight Status and Notification System

This project is a flight status and notification system that updates flight statuses and sends notifications to passengers via SMS. It uses MongoDB to store flight data, Twilio for sending SMS, and RabbitMQ for messaging.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Adding Sample Data](#adding-sample-data)
- [Sending Notifications](#sending-notifications)
- [License](#license)

## Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── flight_data.py
│   ├── notification_service
│   │   ├── __init__.py
│   │   ├── sms_service.py
│   │   ├── rabbitmq_service.py
│   └── main.py
├── venv
├── requirements.txt
└── README.md
```

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/flight-status-notification-system.git
   cd flight-status-notification-system
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure MongoDB and RabbitMQ are running on your machine.**

## Configuration

Edit the `app/config.py` file to set up your configurations:

```python
class Config:
    RABBITMQ_URL = 'amqp://guest:guest@localhost:5672/'
    MONGO_URI = 'mongodb://localhost:27017/flightdb'
    TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
    TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
    TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
    FLIGHT_DATA_URL = 'path_to_your_flight_data.json'
```

## Running the Application

1. **Initialize the database and add sample flights:**

   ```bash
   python app/main.py
   ```

2. **Fetch flight data and update the database:**

   The `fetch_flight_data()` function in `app/flight_data.py` will read from the JSON file specified in `Config.FLIGHT_DATA_URL` and update the flight statuses in the database.

3. **Run the notification services:**

   - **SMS Notification Service:**

     ```bash
     python app/notification_service/sms_service.py
     ```

   - **RabbitMQ Notification Service:**

     ```bash
     python app/notification_service/rabbitmq_service.py
     ```

## Adding Sample Data

To add sample flight data to your database, use the `add_sample_data.py` script:

```python
from app import get_db

def add_sample_data():
    db = get_db()
    sample_flights = [
        {
            "flight_id": "AB123",
            "status": "On Time",
            "gate": "A1",
            "passengers": [
                {"phone_number": "+919027476538"},
                {"phone_number": "+919027476539"}
            ]
        },
        {
            "flight_id": "CD456",
            "status": "Delayed",
            "gate": "B2",
            "passengers": [
                {"phone_number": "+919027476540"}
            ]
        }
    ]
    for flight in sample_flights:
        db.flights.update_one({'flight_id': flight['flight_id']}, {'$set': flight}, upsert=True)

if __name__ == "__main__":
    add_sample_data()
```

Run this script to insert sample data:

```bash
python add_sample_data.py
```

## Sending Notifications

Notifications are sent to passengers based on the data in the MongoDB database. The `sms_service.py` script reads flight data and sends SMS notifications to passengers.

Ensure that the passenger data in your MongoDB collection includes the `phone_number` field for each passenger.

