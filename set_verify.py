from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

import states



async def newAriza_verify_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.lower() == 'ha':
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
                 f"🔎Maqsad: {data.get('goal')}\n")

        await bot.send_message(-1002041326801, f"{ariza}")
        await message.answer("Arizangiz Qabul qilindi✅")
        await state.clear()
    else:
        await message.answer("🤝Yo menga ha deng yoki /stop buyrug'ini yuboring. ")