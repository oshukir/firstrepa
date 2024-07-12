from aiogram.fsm.state import State, StatesGroup

class OrganiseEvent(StatesGroup):
    name = State()
    description = State()
    deadline = State()
    