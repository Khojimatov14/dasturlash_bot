from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.coursesKeyboard import coursesMenu
from loader import dp
from states.allStates import AllStates


@dp.message_handler(text="🔙 Ortga", state=AllStates)
async def boshMenu(message: Message):
    rem = await message.answer(".", reply_markup=ReplyKeyboardRemove())
    await rem.delete()
    await message.answer("O`zingizga kerakli kursni tanlang", reply_markup=coursesMenu)
    await AllStates.courses.set()