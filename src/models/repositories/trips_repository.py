from typing import Dict
from sqlite3 import Connection

class TripsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_trips(self, trips_infos: Dict) -> None: 
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO trips
                    (id, destination, start_date, end_date, owner_name, owner_email)
                VALUES
                    (?, ?, ?, ?, ?, ?)
            ''', (
                trips_infos["id"],
                trips_infos["destination"],
                trips_infos["start_date"],
                trips_infos["end_date"],
                trips_infos["owner_name"],
                trips_infos["owner_email"],
            )
        )
        self.__conn.commit()

    def finf_trip_by_id(self, trip_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
        '''SELECT * FROM trips WHERE id = ?''',(trip_id)
        )
        trip = cursor.fetchone