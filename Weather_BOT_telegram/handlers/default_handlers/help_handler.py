from aiogram import types, Router
from aiogram.filters import Command

router = Router()


@router.message(Command('help'))
async def history_handler(msg: types.Message) -> None:
    """
    Async function for handling messages form telegram user. Has aiogram @router decorator, that catches "/help"
    messages and sends a message back via aiogram Message.reply. Returns list of all commands and explanations on how
    to use them.

    :param msg: Message from telegram user
    :return: None
    """
    text = 'Commands:\n' \
           '/now - "/now" or "/now CITY_NAME" - returns weather in current hour, based on the last city ' \
           'asked, by default Chisianu.\n' \
           '/low - "/low" or "/low CITY_NAME" -  returns hour when temperature is lowest for today.\n ' \
           '/high - "/high" or "/high CITY_NAME" - returns hour when temperature is highest for today.\n' \
           '/custom - "/custom CITY_NAME YYYY-MM-DD HH" - returns forecasted weather for the specified city and time.' \
           'Forecasts are made only for 7 days in advance.'

    await msg.reply('{}'.format(text))
