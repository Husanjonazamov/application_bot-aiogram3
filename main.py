from aiogram import  Bot, Dispatcher, F
from aiogram.types import Message
from asyncio import run
from aiogram.types import BotCommand
from aiogram.filters import  Command
import set_age, set_name, set_phone, set_job,set_verify, set_area, set_goal, set_monthly, set_application_time, set_why_are_you_applying
import set_application_time
import set_area
import set_goal
import set_monthly
import set_verify
import set_why_are_you_applying
import states
import func


dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(5765144405,"Bot ishga tushdi! ✅")


async def shutdown_answer(bot: Bot):
    await bot.send_message(5765144405, "Bot To'xtadi! ❌")


async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.message.register(func.start_command_answer, Command('start'))
    dp.message.register(func.help_command_answer, Command('help'))
    dp.message.register(func.new_command_answer, Command('new'))
    dp.message.register(func.stop_command_answer, Command('stop'))
    dp.message.register(set_why_are_you_applying.newAriza_monthly_answer, states.newAriza.why_are_you_applying)
    dp.message.register(set_name.newAriza_name_answer, states.newAriza.name)
    dp.message.register(set_age.newAriza_age_answer, states.newAriza.age)
    dp.message.register(set_job.newAriza_job_answer, states.newAriza.job)
    dp.message.register(set_area.newAriza_area_answer, states.newAriza.area)
    dp.message.register(set_phone.newAriza_phone_answer, states.newAriza.phone)
    dp.message.register(set_monthly.newAriza_monthly_answer, states.newAriza.monthly)
    dp.message.register(set_application_time.newAriza_application_time_answer, states.newAriza.application_time)
    dp.message.register(set_goal.newAriza_goal_answer, states.newAriza.goal)
    dp.message.register(set_verify.newAriza_verify_answer, states.newAriza.verify)







    bot = Bot('7178118588:AAHMuun6LvJ4lyjObeo7n_S_WmC_H45pWfI')
    await bot.set_my_commands(
        [
            BotCommand(command='/start', description='Botni ishga tushirish'),
            BotCommand(command='/new', description='Yangio ariza qabul qilish'),
            BotCommand(command='/stop', description='Arizani bekor qilish'),
            BotCommand(command='/help', description='Botdan foydalanish uchun yordam'),
        ]
    )
    await dp.start_polling(bot, polling_timeout=1)


run(start())
