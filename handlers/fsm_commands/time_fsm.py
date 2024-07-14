from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import OrganiseEvent
from aiogram.filters import ChatMemberUpdatedFilter, ADMINISTRATOR
from filter import CheckTimeFormat
from typing import Tuple, List


router = Router()

router.chat_member.filter(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR))


@router.message(OrganiseEvent.set_time, F.text, CheckTimeFormat())
async def name_fsm_handler(message: Message, state: FSMContext, time: List[int]):
    await state.set_state(OrganiseEvent.set_image)
    await state.update_data(time=time)
    

    await message.answer("Perfect. Now, appload the preview image for your lottery")
    
@router.message(OrganiseEvent.set_time)
async def name_fsm_handler(message: Message, state: FSMContext):
    await message.answer("No, no, no, my friend. Try to follow next template\n"
                         "HH:MM")