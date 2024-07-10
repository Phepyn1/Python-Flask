
from src.models.settings.db_connection_handler import db_connection_handler
import uuid
from datetime import datetime, timedelta
from src.models.repositories.trips_repository import TripsRepository

db_connection_handler.connect()

def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_infos = {
        "id": str(uuid.uuid4()),
        "destination": "Salvador",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("07-01-2024", "%d-%m-%Y"),
        "owner_name": "Ricardo",
        "owner_email": "ricardo@email.com"
    }
    trips_repository.create_trips(trips_infos)

def test_find_by_id():
    pass

