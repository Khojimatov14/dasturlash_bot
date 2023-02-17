from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.allStates import AllStates
from loader import dp


@dp.message_handler(CommandHelp(), state=AllStates)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/admin - Adminga habar yozish")
    
    await message.answer("\n".join(text))
