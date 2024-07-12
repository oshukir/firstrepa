from aiogram.types import Message, ChatMemberUpdated
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.fsm.state import default_state, any_state
from aiogram.filters import Command, CommandObject, ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import (
    IS_NOT_MEMBER, IS_ADMIN, MEMBER
)


router = Router()
router.my_chat_member.filter(F.chat.type == "group")
router.message.filter(F.chat.type == "group")

@router.message(
    Command("start"),
    ChatMemberUpdatedFilter(member_status_changed=IS_ADMIN)
)
async def cmd_start(message: Message):
    