from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
import states


async def newAriza_age_answer(message: Message, bot: Bot, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) < 150 and int(message.text) > 7:
            await state.update_data(age=message.text)
            await message.answer(f"<b>🕑Yoshingiz qabul qilindi</b>!\n\n<i>👉{message.text}</i>", parse_mode='HTML')
            await message.answer("<b>📚Qanday Texnalogiyalarni bilasiz!</b>", parse_mode='HTML')
            await state.set_state(states.newAriza.job)
        elif int(message.text) > 100 and int(message.text) > 7:
            await message.answer("<b>👨‍🦳Men 100 yoshdan oshgan odam ishga ariza berayotganiga ishonmayman!</b>", parse_mode='HTML')
        else:
            await message.answer("<b>👶Men 7 yoshdan kichkina odam ishga ariza berayotganiga ishonmayman!</b>", parse_mode='HTML')
    else:
        await message.answer("<b>❌Yo'shingizni kiritishda xatolik\n\n"
                             "⏱Misol: 35</b>", parse_mode='HTML')