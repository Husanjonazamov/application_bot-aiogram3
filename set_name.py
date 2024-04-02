from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

import states






async def newAriza_name_answer(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(name=message.text)
    if len(message.text.split()) == 2:
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
            await state.set_state()
            await message.answer(f"<b>👨‍💼Ism-Familyangizni qabul qilindi!</b>\n\n<i>👉{message.text}</i>", parse_mode='HTML')
            await message.answer("<b>🕑Menga Yo'shingini kiriting!</b>", parse_mode='HTML')
            await state.set_state(states.newAriza.age)
        else:
            await message.answer("<b>❌Ism-Familyangizni raqam qatnashishi mumkin emas!</b>", parse_mode='HTML')
    else:
        await message.answer("<b>❌Ism-Familyangizni yuborishda xatolik\n\n"
                             "👨‍💼Misol: Azamov Husanjon</b>", parse_mode='HTML')