from data.config import ADMINS
from loader import dp, bot
from aiogram.types import Message
from states.allStates import AllStates
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands="admin", state=AllStates)
async def adminMessage(message: Message):
    await message.answer("Adminga habar yuboring.")
    await AllStates.messageAdmin.set()

@dp.message_handler(state=AllStates.messageAdmin)
async def sendMessageAdmin(message: Message):
    await bot.send_message(chat_id=ADMINS[0], text=f"TelegramId -> {message.from_user.id}\nUserName -> {message.from_user.full_name} dan habar keldi\n{message.text}")
    await message.answer("Habaringiz adminga yuborildi")
    await AllStates.courses.set()

