from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

coursesMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🐍 Python", callback_data="python")
        ],
        [
            InlineKeyboardButton(text="🛹 Java Script", callback_data="js")
        ],
        [
            InlineKeyboardButton(text="📝 HTML", callback_data="html")
        ],
        [
            InlineKeyboardButton(text="🎨️ CSS", callback_data="css")
        ],
        [
            InlineKeyboardButton(text="🅱️ Bootstrap", callback_data="bootstrap")
        ],
        [
            InlineKeyboardButton(text="👓 Sass", callback_data="sass")
        ],
    ],

)