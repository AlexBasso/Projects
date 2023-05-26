from aiogram import types, Router
from aiogram.filters import Command

from keyboards.reply.start_keyboard import get_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('Welcome to Weather Bot\nFor more info user /help command', reply_markup=get_keyboard())
