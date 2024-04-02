from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

import states


async def start_command_answer(message: Message, bot:Bot):
    await message.answer("<b>🖐Assalomu alaykum, botdan qanday fo'ydalanishni \n🔎bilish uchun <i>/help</i> buyrug'ini yuboring</b>", parse_mode='HTML')


async def help_command_answer(message: Message, bot: Bot):
    matn = """
    <b>📑Botdan Foydalanish:
    🆕/new - yangi ariza yuborish
    🛑/stop - Joriy yuborishni bekor qilish
    </b>
    """
    await message.answer(matn, parse_mode='HTML')

async def new_command_answer(message: Message, state: FSMContext):
    this_state = await state.get_state()
    print(this_state)
    await message.answer("<b>📝Nima uchun murojat qilyapsiz?</b>\n\n<i>📌Masalan: Ish kerak:\nXodim kerak:\nSherik kerak:..</i>", parse_mode='HTML')
    await state.set_state(states.newAriza.why_are_you_applying)



async def stop_command_answer(message: Message, state: FSMContext):
    this_state = await state.get_state()
    if this_state == 'None':
        await message.answer('<b>🛑Bekor qilish uchun ariza mavjud emas!</b>', parse_mode='HTML')
    await message.answer("<b>🛑Joriy ariza bekor qilindi</b>", parse_mode='HTML')
    await state.clear()






