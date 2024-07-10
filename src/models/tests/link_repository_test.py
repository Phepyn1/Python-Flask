from src.models.settings.db_connection_handler import db_connection_handler
import uuid
from src.models.repositories.links_repository import LinkRepository


db_connection_handler.connect()
trip_id = str(uuid.uuid4())

def test_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)
    
    link_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "arroz.com",
        "title": "O Arroz"
    }
    link_repository.create_link(link_infos)
