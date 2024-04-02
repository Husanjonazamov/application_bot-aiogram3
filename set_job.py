from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

import states



async def newAriza_job_answer(message:Message, bot: Bot, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer(f"<b>📚Texnalogiyalaringiz qabul qilindi</b><i>👉{message.text}</i>", parse_mode='HTML')
    await message.answer("<b>📞Telifon raqamni kiriting!</b>\n\n<i>🖋Masalan: +998940014741</i>", parse_mode='HTML')
    await state.set_state(states.newAriza.phone)
