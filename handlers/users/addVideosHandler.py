from aiogram.types import ContentType, Message
from data.config import ADMINS
from loader import db, dp, bot
from states.allStates import AllStates
from aiogram.dispatcher import FSMContext

# Malumotlar omboriga Python video darslik qo`shish
@dp.message_handler(commands="addPythonVideo", user_id=ADMINS)
async def addPy(message: Message):
    # db.deleteVideos()
    count = db.countVideos(language="python")
    await message.answer(f"Python dars videoni yuborishingiz mumkun\nBazada {count[0]} ta video bor")
    await AllStates.addPythonVideo.set()

@dp.message_handler(state=AllStates.addPythonVideo, user_id=ADMINS, content_types=ContentType.VIDEO)
async def addPythonVideos(message: Message, state: FSMContext):
    count = db.countVideos(language="python")
    db.addVideo(videoNum=count[0]+1, language="python", videoName=message.video.file_name, videoFileCode=message.video.file_id)
    await message.answer("Video bazaga qo'shildi")

@dp.message_handler(commands="pythonVideo", user_id=ADMINS)
async def sendPythonVideo(message: Message):
    count = db.countVideos(language="python")
    for i in range(1, count[0]+1):
        video = db.selectVideo(videoNum=i, language="python")
        await message.answer_video(video[4], caption=video[3])

# Malumotlar omboriga HTML video darslik qo`shish
@dp.message_handler(commands="addHTMLVideo", user_id=ADMINS)
async def addHTML(message: Message):
    # db.deleteVideos()
    count = db.countVideos(language="html")
    await message.answer(f"HTML dars videoni yuborishingiz mumkun\nBazada {count[0]} ta video bor")
    await AllStates.addHTMLVideo.set()

@dp.message_handler(state=AllStates.addHTMLVideo, user_id=ADMINS, content_types=ContentType.VIDEO)
async def addHTMLVideos(message: Message, state: FSMContext):
    count = db.countVideos(language="html")
    db.addVideo(videoNum=count[0]+1, language="html", videoName=message.video.file_name, videoFileCode=message.video.file_id)
    await message.answer("Video bazaga qo'shildi")

@dp.message_handler(commands="HTMLVideo", user_id=ADMINS)
async def sendHTMLVideo(message: Message):
    count = db.countVideos(language="html")
    for i in range(1, count[0]+1):
        video = db.selectVideo(videoNum=i, language="html")
        await message.answer_video(video[4], caption=video[3])

# Malumotlar omboriga CSS video darslik qo`shish
@dp.message_handler(commands="addCSSVideo", user_id=ADMINS)
async def addCSS(message: Message):
    # db.deleteVideos()
    count = db.countVideos(language="css")
    await message.answer(f"CSS dars videoni yuborishingiz mumkun\nBazada {count[0]} ta video bor")
    await AllStates.addCSSVideo.set()

@dp.message_handler(state=AllStates.addCSSVideo, user_id=ADMINS, content_types=ContentType.VIDEO)
async def addCSSVideos(message: Message, state: FSMContext):
    count = db.countVideos(language="css")
    db.addVideo(videoNum=count[0]+1, language="css", videoName=message.video.file_name, videoFileCode=message.video.file_id)
    await message.answer("Video bazaga qo'shildi")

@dp.message_handler(commands="CSSVideo", user_id=ADMINS)
async def sendCSSVideo(message: Message):
    count = db.countVideos(language="css")
    for i in range(1, count[0]+1):
        video = db.selectVideo(videoNum=i, language="css")
        await message.answer_video(video[4], caption=video[3])

# Malumotlar omboriga Java Script video darslik qo`shish
@dp.message_handler(commands="addJSVideo", user_id=ADMINS)
async def addJS(message: Message):
    # db.deleteVideos()
    count = db.countVideos(language="js")
    await message.answer(f"Java Script dars videoni yuborishingiz mumkun\nBazada {count[0]} ta video bor")
    await AllStates.addJSVideo.set()

@dp.message_handler(state=AllStates.addJSVideo, user_id=ADMINS, content_types=ContentType.VIDEO)
async def addJSVideos(message: Message, state: FSMContext):
    count = db.countVideos(language="js")
    db.addVideo(videoNum=count[0]+1, language="js", videoName=message.video.file_name, videoFileCode=message.video.file_id)
    await message.answer("Video bazaga qo'shildi")

@dp.message_handler(commands="JSVideo", user_id=ADMINS)
async def sendJSVideo(message: Message):
    count = db.countVideos(language="js")
    for i in range(1, count[0]+1):
        video = db.selectVideo(videoNum=i, language="js")
        await message.answer_video(video[4], caption=video[3])

# Malumotlar omboriga Bootstrap video darslik qo`shish
@dp.message_handler(commands="addBootstrapVideo", user_id=ADMINS)
async def addBootstrap(message: Message):
    # db.deleteVideos()
    count = db.countVideos(language="bootstrap")
    await message.answer(f"Bootstrap dars videoni yuborishingiz mumkun\nBazada {count[0]} ta video bor")
    await AllStates.addBootstrapVideo.set()

@dp.message_handler(state=AllStates.addBootstrapVideo, user_id=ADMINS, content_types=ContentType.VIDEO)
async def addBootstrapVideos(message: Message, state: FSMContext):
    count = db.countVideos(language="bootstrap")
    db.addVideo(videoNum=count[0]+1, language="bootstrap", videoName=message.video.file_name, videoFileCode=message.video.file_id)
    await message.answer("Video bazaga qo'shildi")

@dp.message_handler(commands="bootstrapVideo", user_id=ADMINS)
async def sendSassVideo(message: Message):
    count = db.countVideos(language="bootstrap")
    for i in range(1, count[0]+1):
        video = db.selectVideo(videoNum=i, language="bootstrap")
        await message.answer_video(video[4], caption=video[3])

# Malumotlar omboriga Sass video darslik qo`shish
@dp.message_handler(commands="addSassVideo", user_id=ADMINS)
async def addSass(message: Message):
    # db.deleteVideos()
    count = db.countVideos(language="sass")
    await message.answer(f"Sass dars videoni yuborishingiz mumkun\nBazada {count[0]} ta video bor")
    await AllStates.addSassVideo.set()

@dp.message_handler(state=AllStates.addSassVideo, user_id=ADMINS, content_types=ContentType.VIDEO)
async def addSassVideos(message: Message, state: FSMContext):
    count = db.countVideos(language="sass")
    db.addVideo(videoNum=count[0]+1, language="sass", videoName=message.video.file_name, videoFileCode=message.video.file_id)
    await message.answer("Video bazaga qo'shildi")

@dp.message_handler(commands="sassVideo", user_id=ADMINS)
async def sendSassVideo(message: Message):
    count = db.countVideos(language="sass")
    for i in range(1, count[0]+1):
        video = db.selectVideo(videoNum=i, language="sass")
        await message.answer_video(video[4], caption=video[3])




