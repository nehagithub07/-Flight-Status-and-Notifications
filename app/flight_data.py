from app.models import Flight
from app.config import Config
import json
import logging

logger = logging.getLogger(__name__)

def fetch_flight_data():
    try:
        with open(Config.FLIGHT_DATA_URL, 'r') as file:
            flights = json.load(file)
        for flight in flights:
            Flight.update_flight_status(flight['flight_id'], flight['status'], flight['gate'])
        logger.info("Flight data updated successfully.")
    except FileNotFoundError:
        logger.error(f"Flight data file not found at {Config.FLIGHT_DATA_URL}")
    except json.JSONDecodeError:
        logger.error("Invalid JSON in flight data file")
    except Exception as e:
        logger.error(f"Error fetching flight data: {e}")
        raise