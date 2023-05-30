from database.core import read_last_city_from_db
from utils.check_and_save import check_and_save
from utils.return_weather import weather_req


async def get_weather_response(args: str, user_id: int, msg_text: str, command_word: str,
                               username: str, is_bot: bool) -> str:
    """
    Async function for handling getting weather response from api and database. First checks if there are any arguments
    after the command. If there are no additional arguments, finds last city that was searched for, get current weather
    for it and responds to the user with a string. If there are additional arguments, evaluates if these arguments are
    formatted correctly(if not, responds with a request to fix the format) and provides a response based on the command
    and the argument. On success, saves this request to DB.

    :param args: arguments that come after command "/command args"
    :param user_id: senders unique id
    :param msg_text: entire message, both command and request in a single string '/command request'
    :param command_word: actual command /'command'
    :param username: senders username
    :param is_bot: bool that checks if sender is bot
    :return: string response to telegram user.
    """
    if args is None:
        last_city = read_last_city_from_db(user_id)
        weather_string = "\n".join(weather_req(last_city, command_word))
        bot_response = 'Weather in ' + str(last_city) + ':\n' + weather_string
        await check_and_save(args='', msg=msg_text, command_word=command_word,
                             username=username, userid=user_id,
                             bot_response=bot_response, is_bot=is_bot, last_city=last_city)
        return bot_response

    else:
        bot_response = 'Weather in ' + str(args) + ':\n'
        try:
            weather_string = "\n".join(weather_req(args, command_word))
        except KeyError or ValueError:
            bot_response = 'City with this name is not known, try a different city name.'
        else:
            bot_response += weather_string
            await check_and_save(args=args, msg=msg_text, command_word=command_word,
                                 username=username, userid=user_id,
                                 bot_response=bot_response, is_bot=is_bot, last_city=args)
        return bot_response
