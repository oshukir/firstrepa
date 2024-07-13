from aiogram.types import Message, ChatMemberUpdated
from aiogram.fsm.context import FSMContext
from aiogram import Router, F, Bot
from aiogram.fsm.state import default_state, any_state
from aiogram.filters import Command, CommandObject, ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import (
    MEMBER, ADMINISTRATOR, IS_MEMBER, IS_NOT_MEMBER, IS_ADMIN,
    JOIN_TRANSITION
)


router = Router()

router.my_chat_member.filter(F.chat.type.in_({"group", "supergroup"}))
router.message.filter(F.chat.type.in_({"group", "supergroup"}))


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=IS_NOT_MEMBER >> ADMINISTRATOR
    )
)
async def bot_added_as_admin(event: ChatMemberUpdated, chat_ids_with_adm: dict, bot:Bot):
    await event.answer(
        text=f"I see you read all requirements to my complete work here\n"
             f"Thanks for adding me in the group: {event.chat.title}"
             f"Press /start to organise lottery (it is only available to admins)"
    )
    admins = await bot.get_chat_administrators(event.chat.id)
    admins_ids = [admin.user.id for admin in admins]
    chat_ids_with_adm[event.chat.id] = admins_ids




@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=IS_MEMBER >> ADMINISTRATOR
    )
)
async def bot_added_as_admin(event: ChatMemberUpdated, chat_ids_with_adm: dict, bot:Bot):
    admins = await bot.get_chat_administrators(event.chat.id)
    admins_ids = [admin.user.id for admin in admins]
    chat_ids_with_adm[event.chat.id] = admins_ids

    await event.answer(
        text=f"Good job, buddy. Now, it is time to make events.\n"
             f"Press /start to organise lottery (it is only available to admins)"
    )


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=IS_NOT_MEMBER >> MEMBER
    )
)
async def bot_added_as_member(event : ChatMemberUpdated, bot : Bot):
    chat_info = await bot.get_chat(event.chat.id)
    if chat_info.permissions.can_send_messages:
        await event.answer(
            text=f"You are such a full, and bloody greedy man.\n"
                 f"Try to promote me to admin for my functional work in this group"
        )
        
