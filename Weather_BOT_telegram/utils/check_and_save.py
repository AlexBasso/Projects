from database.core import save_to_db


async def check_and_save(args: str, msg: str, command_word: str, username: str, userid: int, bot_response: str,
                         is_bot: bool, last_city: str = 'Chisinau') -> None:
    """
    Async function that checks if received message is a command and that the sender is not a bot. Checks that last_city
    is actualy name and not a string. Calls function save_to_db with all the parameters for actual saving to DB.

    :param args: arguments that come after command "/command args"
    :param msg: entire message, both command and request in a single string '/command request'
    :param command_word: actual command /'command'
    :param username: senders username
    :param userid: senders unique id
    :param bot_response: response that bot gives to the users '/command request'
    :param is_bot: bool that checks if sender is bot
    :param last_city: Last city to be called for weather update, by default Chisinau.
    :return: None
    """

    if not is_bot and msg.startswith('/{}'.format(command_word)):
        if len(last_city.split()) > 1:
            last_city = args.split()[0]
        save_to_db(request=args, name=username, sender_id=userid, command=command_word,
                   bot_response=bot_response, last_city=last_city)
