from aiogram import types, Router
from aiogram.filters import Command, CommandObject

from handlers.custom_handlers.weather_handler import get_weather_response

router = Router()


@router.message(Command(commands=['now', 'low', 'high', 'custom']))
async def basic_functions_handler(msg: types.Message, command: CommandObject) -> None:
    """
    Async function for handling messages form telegram user. Has aiogram @router decorator, that catches "/'now', 'low',
    'high', 'custom'" messages and sends a message back via aiogram Message.reply. Commands:
    /now - "/now" or "/now CITY_NAME" - returns weather in current hour, based on the last city asked, default Chisianu.
    /low - "/low" or "/low CITY_NAME" -  returns hour when temperature is lowest for today.
    /high - "/high" or "/high CITY_NAME" - returns hour when temperature is highest for today.
    /custom - "/custom CITY_NAME YYYY-MM-DD HH" - returns forecasted weather for the specified city and time. Forecasts
    are made only for 7 days in advance.

    :param msg: Message from telegram user
    :param command: CommandObject - text after command "/'now', 'low',
    'high', 'custom'"
    :return: None
    """
    bot_response = await get_weather_response(args=command.args, user_id=msg.from_user.id, msg_text=msg.text,
                                              command_word=command.command, username=msg.from_user.full_name,
                                              is_bot=msg.from_user.is_bot)
    await msg.reply(bot_response)
