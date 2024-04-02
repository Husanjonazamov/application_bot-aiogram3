from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

import states



async def newAriza_goal_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(goal=message.text)
    await message.answer(f"<b>Maqsadingiz qabul qilindi\n\n👉{message.text}</b>", parse_mode='HTML')
    data = await state.get_data()
    ariza = (f"{data.get("why_are_you_applying")}\n\n"
             f"👨‍💼Xodim: {data.get('name')}\n"
             f"🕑Yosh: {data.get('age')}\n"
             f"📚Texnalogiya: {data.get('job')}\n"
             f"🇺🇿Telegram: @{message.from_user.username}\n"
             f"📞Aloqa: {data.get('phone')}\n"
             f"🌐Hudud: {data.get('area')}\n"
             f"💰Narxi: {data.get('monthly')}\n"
             f"🕰Murojat qilish Vaqti: {data.get('application_time')}\n"
             f"🔎Maqsad: {message.text}\n")
    await message.answer(f"Ariza Yuboraveraymi?\n\n{ariza}\n\nHa yoki /stop deb yuboring")
    await state.set_state(states.newAriza.verify)
