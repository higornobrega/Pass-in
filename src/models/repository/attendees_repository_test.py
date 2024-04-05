import pytest

from src.models.settings.connection import db_connection_handler

from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()
@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    event_id = "meu-uuid-e-nois66"
    attendees_info = {
        "uuid": "meu-uuid-e-nois66",
        'name': 'meu name',
        'email': 'email@email.com',
        'event_id': event_id,
    }
    attendees_repository = AttendeesRepository()

    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="Não necessita")
def test_get_attendees_badge_by_id():
    attendee_id = "meu-uuid-e-nois66"
    attendees_repository = AttendeesRepository()

    attendee = attendees_repository.get_attendees_badge_by_id(attendee_id)
    print(attendee)