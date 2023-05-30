from aiogram import types, Router

router = Router()


@router.message()
async def hello_handler(msg: types.Message) -> None:
    """
    Async function for handling messages form telegram user. Has aiogram @router decorator, that catches any messages
    and sends a message back via aiogram Message.reply. This function catches all messages, but responds only to
    users "Hello" message.

    :param msg: Message form telegram user.
    :return: None
    """
    if msg.text == 'Привет':
        await msg.reply(f'Привет {msg.from_user.full_name},\nпопробуй /help для большей информации о боте')
