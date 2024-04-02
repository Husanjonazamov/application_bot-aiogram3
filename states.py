from aiogram.fsm.state import State, StatesGroup


class newAriza(StatesGroup):
    why_are_you_applying = State()
    name = State()
    age = State()
    job = State()
    phone = State()
    area = State()
    monthly = State()
    application_time = State()
    goal = State()
    verify = State()