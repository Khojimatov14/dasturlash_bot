from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuVideo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Oldingi"),
            KeyboardButton(text="Keyingi ➡️"),
        ],
        [
            KeyboardButton(text="🔙 Ortga"),
        ],
    ],
    resize_keyboard=True
)