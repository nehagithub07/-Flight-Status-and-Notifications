from app import mongo
import logging

logger = logging.getLogger(__name__)

class Flight:
    @staticmethod
    def get_all_flights():
        try:
            flights = list(mongo.db.flights.find({}, {'_id': 0}))
            return flights
        except Exception as e:
            logger.error(f"Error fetching all flights: {e}")
            return []

    @staticmethod
    def get_flight_by_id(flight_id):
        try:
            flight = mongo.db.flights.find_one({'flight_id': flight_id}, {'_id': 0})
            return flight
        except Exception as e:
            logger.error(f"Error fetching flight by ID {flight_id}: {e}")
            return None

    @staticmethod
    def update_flight_status(flight_id, status, gate):
        try:
            result = mongo.db.flights.update_one(
                {'flight_id': flight_id},
                {'$set': {'status': status, 'gate': gate}},
                upsert=True
            )
            if result.modified_count > 0:
                logger.info(f"Flight status updated for ID {flight_id}.")
            elif result.upserted_id:
                logger.info(f"New flight created with ID {flight_id}.")
            return True
        except Exception as e:
            logger.error(f"Error updating flight status for ID {flight_id}: {e}")
            return False