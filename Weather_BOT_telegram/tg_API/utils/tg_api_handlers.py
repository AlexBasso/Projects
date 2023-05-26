from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command('hello-world'))
async def start_handler(msg: Message) -> None:
    """
    Async method for handling messages form telegram user. Has @router decorator, that catches "/start" messages and
    sends message back via aiogram Message.answer.

    :param msg: Message form telegram user.
    :return: None
    """
    await msg.answer('Hello World!\nHere you can get information about weather!')



@router.message()
async def start_handler(msg: Message) -> None:
    """
    Async method for handling messages form telegram user. Has @router decorator, that catches any messages and
    sends message back via aiogram Message.answer.

    :param msg: Message form telegram user.
    :return: None
    """
    if msg.text == 'Привет':
        await msg.answer('ok')

# @router.message(Command("low"))
# async def message_handler(msg: Message):
#     await msg.answer(f" low as a test sending you your ID: {msg.from_user.id}")
