import asyncio
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.default.changeCoursKeyboard import menuVideo
from keyboards.inline.coursesKeyboard import coursesMenu
from loader import dp, db
from states.allStates import AllStates

@dp.callback_query_handler(text="sass", state=AllStates.courses)
async def sendPythonVideo(call: CallbackQuery):
    user = db.selectUser(userId=call.from_user.id)
    if user[13] == 1:
        await call.message.answer("Siz Sass kursini tanladingiz\nO`qituvchi: <b>Ulug`bek Samig`jonov</b>")
    await call.message.delete()
    user = db.selectUser(userId=call.from_user.id)
    video = db.selectVideo(videoNum=user[13], language="sass")
    await call.message.answer_video(video[4], caption=video[3], reply_markup=menuVideo)
    await AllStates.sass.set()
    await call.answer(cache_time=60)

@dp.message_handler(text="Keyingi ➡️", state=AllStates.sass)
async def keyingiVideo(message: Message):
    count = db.countVideos(language="sass"); count = count[0]
    user = db.selectUser(userId=message.from_user.id)
    if user[13] < count:
        video = db.selectVideo(videoNum=user[13]+1, language="sass")
        await message.answer_video(video[4], caption=video[3])
        db.updateUserLastVideoSass(newVideo=user[13]+1, userId=message.from_user.id)
    else:
        rem = await message.answer("Siz Sass kursidagi barcha video darsliklarni ko`rib bo`ldingiz!")
        await asyncio.sleep(5)
        await message.delete()
        await rem.delete()

@dp.message_handler(text="⬅️ Oldingi", state=AllStates.sass)
async def oldingiVideo(message: Message):
    user = db.selectUser(userId=message.from_user.id)
    if user[13] > 1:
        video = db.selectVideo(videoNum=user[13]-1, language="sass")
        await message.answer_video(video[4], caption=video[3])
        db.updateUserLastVideoSass(newVideo=user[13]-1, userId=message.from_user.id)
    else:
        rem = await message.answer("Bu birinchi video darslik iltimos keyingi videoga o`ting!")
        await asyncio.sleep(5)
        await message.delete()
        await rem.delete()

@dp.message_handler(state=AllStates.sass)
async def boshMenu(message: Message):
    rem = await message.answer("Bu yerda habar yozishingiz mumkun emas iltimos darsdan chalg`imang!")
    await asyncio.sleep(5)
    await message.delete()
    await rem.delete()