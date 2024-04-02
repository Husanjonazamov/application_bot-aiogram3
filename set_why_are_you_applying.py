from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

import states



async def newAriza_monthly_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(why_are_you_applying=message.text)
    if len(message.text.split()) > 1:
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
                await message.answer("📝Murojatni matn o'rqali Kiriting")
        else:
            await message.answer(f"<b>📃Murojat qabul qilindi\n\n👉{message.text}</b>", parse_mode='HTML')
            await message.answer("<b>👨‍💼Ism-Familyangizni kiriting</b>", parse_mode='HTML')
            await state.set_state(states.newAriza.name)
    else:
        await message.answer("📝Murojat kamida 2 ta so'zdan iborat bo'lishi kerak")