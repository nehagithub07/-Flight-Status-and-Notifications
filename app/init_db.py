from app import app
from app.database import mongo
import logging

logger = logging.getLogger(__name__)

def init_db():
    with app.app_context():
        try:
            # Clear existing data
            mongo.db.flights.delete_many({})

            # Insert sample data
            sample_flights = [
                {"flight_id": "AA123", "status": "On Time", "gate": "A10"},
                {"flight_id": "BA456", "status": "Delayed", "gate": "B5"},
                {"flight_id": "UA789", "status": "Boarding", "gate": "C15"}
            ]
            for flight in sample_flights:
                mongo.db.flights.update_one(
                    {"flight_id": flight['flight_id']},
                    {"$set": flight},
                    upsert=True
                )
            logger.info("Database initialized with sample data.")
        except Exception as e:
            logger.error(f"Error initializing database: {e}")