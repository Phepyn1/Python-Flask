from typing import Dict
from sqlite3 import Connection

class LinkRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_link(self, link_infos: Dict) -> None: 
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, trip_id, link, title)
                VALUES
                    (?, ?, ?, ?)
            ''', (
                link_infos["id"],
                link_infos["trip_id"],
                link_infos["link"],
                link_infos["title"],
            )
        )
        self.__conn.commit()