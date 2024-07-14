from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import OrganiseEvent
from aiogram.filters import ChatMemberUpdatedFilter, ADMINISTRATOR


router = Router()

router.chat_member.filter(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR))


@router.message(OrganiseEvent.set_description, F.text.func(len) <= 50)
async def name_fsm_handler(message: Message, state: FSMContext):
    await state.set_state(OrganiseEvent.set_prize)
    await state.update_data(description=message.text)

    await message.answer("Good job, buddy. Now give me the name of prize in 15 characters")

@router.message(OrganiseEvent.set_description)
async def name_fsm_handler(message: Message, state: FSMContext):
    await message.answer("Bad job, dude. Please restrict the description in range of 50 characters")