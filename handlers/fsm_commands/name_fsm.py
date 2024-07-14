from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import OrganiseEvent
from aiogram.filters import ChatMemberUpdatedFilter, ADMINISTRATOR


router = Router()

router.chat_member.filter(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR))


@router.message(OrganiseEvent.set_name)
async def name_fsm_handler(message: Message, state: FSMContext):
    await state.set_state(OrganiseEvent.set_description)
    await state.update_data(name=message.text)

    await message.answer("Give me small description of lottery at max of 50 characters")
