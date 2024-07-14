from aiogram.fsm.state import State, StatesGroup

class OrganiseEvent(StatesGroup):
    set_name = State()
    set_prize = State()
    set_description = State()
    set_image = State()
    set_date = State()
    set_time = State()
 
