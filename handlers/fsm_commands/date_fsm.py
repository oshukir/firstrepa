from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import OrganiseEvent
from aiogram.filters import ChatMemberUpdatedFilter, ADMINISTRATOR
from filter import CheckDateFormat
from typing import Tuple, List


router = Router()

router.chat_member.filter(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR))


@router.message(OrganiseEvent.set_date, F.text, CheckDateFormat())
async def name_fsm_handler(message: Message, state: FSMContext, date: List[int]):
    await state.set_state(OrganiseEvent.set_time)
    await state.update_data(date=date)
    

    await message.answer("Perfect. Now, enter the time deadline as next template\n"
                         "hh:mm")
    
@router.message(OrganiseEvent.set_date)
async def name_fsm_handler(message: Message, state: FSMContext):
    await message.answer("No, no, no, my friend. Try to follow next template\n"
                         "dd/mm/yy")