import asyncio
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.default.changeCoursKeyboard import menuVideo
from keyboards.inline.coursesKeyboard import coursesMenu
from loader import dp, db
from states.allStates import AllStates

@dp.callback_query_handler(text="css", state=AllStates.courses)
async def sendPythonVideo(call: CallbackQuery):
    user = db.selectUser(userId=call.from_user.id)
    if user[7] == 1:
        await call.message.answer("Siz CSS kursini tanladingiz\nO`qituvchi: <b>Ulug`bek Samig`jonov</b>")
    await call.message.delete()
    user = db.selectUser(userId=call.from_user.id)
    video = db.selectVideo(videoNum=user[7], language="css")
    await call.message.answer_video(video[4], caption=video[3], reply_markup=menuVideo)
    await AllStates.css.set()
    await call.answer(cache_time=60)

@dp.message_handler(text="Keyingi ➡️", state=AllStates.css)
async def keyingiVideo(message: Message):
    count = db.countVideos(language="css"); count = count[0]
    user = db.selectUser(userId=message.from_user.id)
    if user[7] < count:
        video = db.selectVideo(videoNum=user[7]+1, language="css")
        await message.answer_video(video[4], caption=video[3])
        db.updateUserLastVideoCSS(newVideo=user[7]+1, userId=message.from_user.id)
    else:
        rem = await message.answer("Siz CSS kursidagi barcha video darsliklarni ko`rib bo`ldingiz!")
        await asyncio.sleep(5)
        await message.delete()
        await rem.delete()

@dp.message_handler(text="⬅️ Oldingi", state=AllStates.css)
async def oldingiVideo(message: Message):
    user = db.selectUser(userId=message.from_user.id)
    if user[7] > 1:
        video = db.selectVideo(videoNum=user[7]-1, language="css")
        await message.answer_video(video[4], caption=video[3])
        db.updateUserLastVideoCSS(newVideo=user[7]-1, userId=message.from_user.id)
    else:
        rem = await message.answer("Bu birinchi video darslik iltimos keyingi videoga o`ting!")
        await asyncio.sleep(5)
        await message.delete()
        await rem.delete()

@dp.message_handler(state=AllStates.css)
async def boshMenu(message: Message):
    rem = await message.answer("Bu yerda habar yozishingiz mumkun emas iltimos darsdan chalg`imang!")
    await asyncio.sleep(5)
    await message.delete()
    await rem.delete()