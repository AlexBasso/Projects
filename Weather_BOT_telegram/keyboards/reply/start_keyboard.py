from aiogram import types


def get_keyboard():
    kb = [
        [
            types.KeyboardButton(text="/now"),
        ],
        [
            types.KeyboardButton(text="/low"),
            types.KeyboardButton(text="/high"),
            types.KeyboardButton(text="/custom")
        ],
        [
            types.KeyboardButton(text="/history"),
            types.KeyboardButton(text="/help"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Choose a command"
    )
    return keyboard
