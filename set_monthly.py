from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

import states



async def newAriza_monthly_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(monthly=message.text)
    if not ("0" in message.text or
            "1" in message.text or
            "2" in message.text or
            "3" in message.text or
            "4" in message.text or
            "5" in message.text or
            "6" in message.text or
            "7" in message.text or
            "8" in message.text or
            "9" in message.text):
        await message.answer("📝Iltimos raqamda kiriting")
    else:
        await message.answer(f"<b>💰Narx qabul qilindi\n\n👉{message.text}</b>", parse_mode='HTML')
        await message.answer("<b>🕰Sizga Murojat qilish vaqtini kiriting!</b>\n\n<i>⏳Masalan: 9:00-20:00</i>", parse_mode='HTML')
        await state.set_state(states.newAriza.application_time)