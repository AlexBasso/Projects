from aiogram import types, Router
from aiogram.filters import Command, CommandObject

from utils.check_and_save import check_and_save

router = Router()
command_word = 'hello-world'


@router.message(Command(command_word))
async def start_handler(msg: types.Message, command: CommandObject) -> None:
    """
    Async function for handling messages form telegram user. Has aiogram @router decorator, that catches "/start"
    messages and sends a message back via aiogram Message.reply.

    :param msg: Message from telegram user
    :param command: CommandObject - text after command /hello-world
    :return: None
    """
    bot_response = 'Hello World!\nHere you can get information about weather!'
    await check_and_save(args=command.args, msg=msg.text, command_word=command_word, username=msg.from_user.full_name,
                         userid=msg.from_user.id, bot_response=bot_response, is_bot=msg.from_user.is_bot)

    await msg.reply(bot_response)
