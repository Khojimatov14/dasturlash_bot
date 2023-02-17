import asyncio
import logging
from aiogram.utils.exceptions import BotBlocked
from loader import dp, db, bot
from data.config import ADMINS
from aiogram.types import Message
from states.allStates import AllStates

@dp.message_handler(commands="startMessage", user_id=ADMINS, state=AllStates)
async def startMessage(message: Message):
    realUsers = 0
    for user in db.selectAllUsers():
        try:
            await bot.send_message(chat_id=user[0], text="Noqulaylik uchun uzur so`rayman\nBo`t qayta ishga tushdi iltimos /start buyrug`ini kiriting!")
            await asyncio.sleep(0.3)
            realUsers += 1
        except BotBlocked:
            logging.error(f"Bot was blocked by user with id: {user[0]}")
    await message.answer(f"Botdan hozirda {realUsers} ta haqiqiy foydalanuvchilar foydalanmoqda!")

@dp.message_handler(commands="chackUsers", user_id=ADMINS, state=AllStates)
async def stop_handler(message: Message):
    realUsers = 0
    for user in db.selectAllUsers():
        try:
            rem = await bot.send_message(chat_id=user[0],text="sorry")
            await asyncio.sleep(0.3)
            await rem.delete()
            realUsers += 1
        except BotBlocked:
            logging.error(f"Bot was blocked by user with id: {user[0]}")
    await message.answer(f"Botdan hozirda {realUsers} ta haqiqiy foydalanuvchilar foydalanmoqda!")

@dp.message_handler(commands="countUsers", user_id=ADMINS, state=AllStates)
async def startMessage(message: Message):
    await message.answer(f"Bazada <b>{db.countUsers()[0]} ta</b> foydalanuvchilar bor.")
