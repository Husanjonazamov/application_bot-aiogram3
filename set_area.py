from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

import states



async def newAriza_area_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(area=message.text)
    if ("0" in message.text or
            "1" in message.text or
            "2" in message.text or
            "3" in message.text or
            "4" in message.text or
            "5" in message.text or
            "6" in message.text or
            "7" in message.text or
            "8" in message.text or
            "9" in message.text):
            await message.answer("📝Hududni matn o'rqali Tushuntiring")
    else:
        await message.answer(f"<b>Hudud qabul qilindi\n\n👉{message.text}</b>", parse_mode='HTML')
        await message.answer("<b>💰Oylik maoshingiz narxini kiriting</b>", parse_mode='HTML')
        await state.set_state(states.newAriza.monthly)