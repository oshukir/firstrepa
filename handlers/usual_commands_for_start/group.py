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

@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=
        (IS_NOT_MEMBER | MEMBER) 
        >>
        (IS_ADMIN)
    )
)
async def bot_added_or_promoted_as_admin(event: ChatMemberUpdated):
    await event.answer(
        text=f"I see you read all requirements to my complete work here"
             f"Thanks for addint me in group: {event.chat.title}"
    )

@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=
        (IS_NOT_MEMBER)
        >>
        (MEMBER)
    )
)
async def bot_added_ad_member(event : ChatMemberUpdated):
    await event.answer(
        text=f"You are such a full, and bloody greedy man."
             f"Try to promote me to admin for my functional work in this group"
    )