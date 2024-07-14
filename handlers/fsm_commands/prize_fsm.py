from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import OrganiseEvent
from aiogram.filters import ChatMemberUpdatedFilter, ADMINISTRATOR


router = Router()

router.chat_member.filter(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR))


@router.message(OrganiseEvent.set_prize, F.text.func(len) <= 15)
async def name_fsm_handler(message: Message, state: FSMContext):
    await state.set_state(OrganiseEvent.set_date)
    await state.update_data(prize=message.text)

    await message.answer("Such a good boy. Please, enter the date of deadline as next template\n"
                         "dd/mm/yy")
    
@router.message(OrganiseEvent.set_prize)
async def name_fsm_handler(message: Message, state: FSMContext):
    await message.answer("No, no, no, my friend. What are you doing? Please place at maximum 15 characters in prize section")