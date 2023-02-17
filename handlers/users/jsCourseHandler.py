import asyncio

from aiogram.types import CallbackQuery
from loader import dp
from states.allStates import AllStates

@dp.callback_query_handler(text="js", state=AllStates.courses)
async def sendPythonVideo(call: CallbackQuery):
    msg = await call.message.answer("Tez Orada JavaScript Darslari Qo`shiladi!")
    await asyncio.sleep(5)
    await msg.delete()
    await call.answer(cache_time=60)