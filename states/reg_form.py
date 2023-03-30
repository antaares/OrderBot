

from aiogram.dispatcher.filters.state import State, StatesGroup





class LangForm(StatesGroup):
    language = State()




class RegForm(StatesGroup):
    full_name = State()
    age = State()
    from_where = State()
    course = State()
    lesson_type = State()
    phone_number = State()