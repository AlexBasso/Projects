from database.models import db, History
from database.database_CRUD import CRUDInterface

db.connect()
db.create_tables([History], safe=True)

crud = CRUDInterface()


def save_to_db(name: str, request: str, sender_id: int, command: str, bot_response: str,
               last_city: str = 'Chisinau') -> None:
    """
    Function for saving messages to DB. Takes in params and sends them to create() function for saving.

    :param name: names of user that sent the message
    :param request: specifics of the request after the command '/command specifics'
    :param sender_id: users unique id
    :param command: used '/command '
    :param bot_response: response given by bot for this '/command request'
    :param last_city: Last city to be called for weather update, by default Chisinau.
    :return: None
    """
    data = [{'name': name, 'request': request, 'sender_id': sender_id,
             'command': command, 'bot_response': bot_response, 'last_city': last_city}]
    db_write = crud.create()
    db_write(db, History, data)


def read_from_db(sender_id: int) -> str:
    """
    Function that takes last 10 requests made by this specific user. Takes in params(user id) and sends them to
    retrieve() function that returns the requested data. This data is formatted in to presentable string and returned.

    :param sender_id: user unique id
    :return: str
    """
    db_read = crud.retrieve()
    retrieve = db_read(db, History, History.created_at, History.name, History.id,
                       History.command, History.request, History.bot_response).where(History.sender_id == sender_id)
    temp_list_entries_from_db = []

    for one_entry_form_db in retrieve:
        if one_entry_form_db.request is None:
            one_entry_form_db.request = ''
        temp_string = '{0}  -  {1}\nCommand: /{2} {3}\nResponse: {4}\n'.format(
            str(one_entry_form_db.created_at), one_entry_form_db.name, one_entry_form_db.command,
            one_entry_form_db.request, one_entry_form_db.bot_response)
        temp_list_entries_from_db.append(temp_string)

    response_data = '\n'.join(temp_list_entries_from_db)

    return response_data


def read_last_city_from_db(sender_id: int) -> str:
    """
    Function that takes last 10 requests made by this specific user(user id) and returns last city name, that was used
    successfully in a command. Last successful entry is found via primary key(id). If no entries, default = Chisinau.

    :param sender_id: user unique id
    :return: str
    """
    db_read = crud.retrieve()
    retrieve = db_read(db, History, History.created_at, History.last_city).where(History.sender_id == sender_id)
    try:
        retrieve = retrieve[0].last_city
    except IndexError:
        retrieve = 'Chisinau'

    return retrieve
