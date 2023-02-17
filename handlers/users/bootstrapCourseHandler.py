import asyncio
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.default.changeCoursKeyboard import menuVideo
from keyboards.inline.coursesKeyboard import coursesMenu
from loader import dp, db
from states.allStates import AllStates

@dp.callback_query_handler(text="bootstrap", state=AllStates.courses)
async def sendPythonVideo(call: CallbackQuery):
    user = db.selectUser(userId=call.from_user.id)
    if user[10] == 1:
        await call.message.answer("Siz Bootstrap kursini tanladingiz\nO`qituvchi: <b>Ulug`bek Samig`jonov</b>")
    await call.message.delete()
    user = db.selectUser(userId=call.from_user.id)
    video = db.selectVideo(videoNum=user[10], language="bootstrap")
    await call.message.answer_video(video[4], caption=video[3], reply_markup=menuVideo)
    await AllStates.bootstrap.set()
    await call.answer(cache_time=60)

@dp.message_handler(text="Keyingi ➡️", state=AllStates.bootstrap)
async def keyingiVideo(message: Message):
    count = db.countVideos(language="bootstrap"); count = count[0]
    user = db.selectUser(userId=message.from_user.id)
    if user[10] < count:
        video = db.selectVideo(videoNum=user[10]+1, language="bootstrap")
        await message.answer_video(video[4], caption=video[3])
        db.updateUserLastVideoBootstrap(newVideo=user[10]+1, userId=message.from_user.id)
    else:
        rem = await message.answer("Siz Bootstrap kursidagi barcha video darsliklarni ko`rib bo`ldingiz!")
        await asyncio.sleep(5)
        await message.delete()
        await rem.delete()

@dp.message_handler(text="⬅️ Oldingi", state=AllStates.bootstrap)
async def oldingiVideo(message: Message):
    user = db.selectUser(userId=message.from_user.id)
    if user[10] > 1:
        video = db.selectVideo(videoNum=user[10]-1, language="bootstrap")
        await message.answer_video(video[4], caption=video[3])
        db.updateUserLastVideoBootstrap(newVideo=user[10]-1, userId=message.from_user.id)
    else:
        rem = await message.answer("Bu birinchi video darslik iltimos keyingi videoga o`ting!")
        await asyncio.sleep(5)
        await message.delete()
        await rem.delete()

@dp.message_handler(state=AllStates.bootstrap)
async def boshMenu(message: Message):
    rem = await message.answer("Bu yerda habar yozishingiz mumkun emas iltimos darsdan chalg`imang!")
    await asyncio.sleep(5)
    await message.delete()
    await rem.delete()