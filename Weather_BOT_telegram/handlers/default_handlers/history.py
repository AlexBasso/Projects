from aiogram import types, Router
from aiogram.filters import Command

from database.core import read_from_db

router = Router()


@router.message(Command('history'))
async def history_handler(msg: types.Message) -> None:
    """
    Async function for handling messages form telegram user. Has aiogram @router decorator, that catches "/history"
    messages and sends a message back via aiogram Message.reply. Returns history of last 10 previous commands.

    :param msg: Message from telegram user
    :return: None
    """
    text = read_from_db(msg.from_user.id)

    await msg.reply('This is Your last 10 history commands:\n{}'.format(text))
