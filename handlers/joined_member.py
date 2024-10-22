from aiogram import F, Router
from aiogram.filters.chat_member_updated import (
    ChatMemberUpdatedFilter, JOIN_TRANSITION, IS_NOT_MEMBER, IS_MEMBER, IS_ADMIN, ADMINISTRATOR
)
from aiogram.types import ChatMemberUpdated

router = Router()
router.chat_member.filter(F.chat.type.in_({"group", "supergroup"}))


@router.chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=
        (IS_NOT_MEMBER)
        >>
        IS_ADMIN
    )
)
@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=ADMINISTRATOR
    )
)
async def left_event_handler(event: ChatMemberUpdated, chat_ids_with_players: dict, chat_ids_with_adm: dict):
    chat_ids_with_adm[event.chat.id].append(event.new_chat_member.user.id)

    print(chat_ids_with_adm[event.chat.id])
    await event.answer(text="THE admin is added")





@router.chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=
        (IS_MEMBER)
        >>
        IS_ADMIN
    )
)
@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=ADMINISTRATOR
    )
)
async def left_event_handler(event: ChatMemberUpdated, chat_ids_with_players: dict, chat_ids_with_adm: dict):
    chat_ids_with_adm[event.chat.id].append(event.new_chat_member.user.id)

    print(event.new_chat_member.user.id)
    print(chat_ids_with_adm[event.chat.id])
    await event.answer(text="THE admin is added")






@router.chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=
        (IS_NOT_MEMBER)
        >>
        IS_MEMBER
    )
)
@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=ADMINISTRATOR
    )
)
async def left_event_handler(event: ChatMemberUpdated, chat_ids_with_players: dict):
    
    await event.answer(text="THE member is added")
