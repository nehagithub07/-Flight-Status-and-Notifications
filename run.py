from app import create_app
from app.config import Config
from app.database import init_db
from app.notification_service.rabbitmq import start_rabbitmq_consumer
from app.flight_data import fetch_flight_data
import threading
import schedule
import time

app = create_app(Config)

def update_flight_data():
    with app.app_context():
        fetch_flight_data()

def run_schedule():
    schedule.every(30).minutes.do(update_flight_data)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    with app.app_context():
        init_db(app)  # Pass the app to init_db
        fetch_flight_data()

    # Start RabbitMQ consumer in a separate thread
    rabbitmq_thread = threading.Thread(target=start_rabbitmq_consumer)
    rabbitmq_thread.daemon = True
    rabbitmq_thread.start()

    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=run_schedule)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    # Run the Flask app
    app.run(debug=True)