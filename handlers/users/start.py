import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from keyboards.inline.coursesKeyboard import coursesMenu
from loader import dp, db, bot
from states.allStates import AllStates


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        db.addUsers(userId=message.from_user.id,
                    userName=message.from_user.username,
                    userFullName=message.from_user.full_name,
                    userPhoneNumber=1234567,
                    userLastVideoNumberPython=1,
                    userLastVideoNumberJS=1,
                    userLastVideoNumberHTML=1,
                    userLastVideoNumberCSS=1,
                    userLastVideoNumberJava=1,
                    userLastVideoNumberCPlusPlus=1,
                    userLastVideoNumberBootstrap=1,
                    userLastVideoNumberDoteNet=1,
                    userLastVideoNumberDjango=1,
                    userLastVideoNumberSass=1)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    count = db.countUsers()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

    await message.answer(f"Salom, {message.from_user.full_name}!\n O`zingizga kerakli kursni tanlang", reply_markup=coursesMenu)
    await AllStates.courses.set()

@dp.message_handler(CommandStart(), state=AllStates)
async def bot_start_state(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n O`zingizga kerakli kursni tanlang", reply_markup=coursesMenu)
    await AllStates.courses.set()

