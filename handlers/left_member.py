from aiogram import F, Router
from aiogram.filters.chat_member_updated import (
    ChatMemberUpdatedFilter, JOIN_TRANSITION, IS_NOT_MEMBER, IS_MEMBER, IS_ADMIN, ADMINISTRATOR
)
from aiogram.types import ChatMemberUpdated
from typing import Dict, List

router = Router()
router.chat_member.filter(F.chat.type.in_({"group", "supergroup"}))


@router.chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=
        (IS_ADMIN)
        >>
        IS_NOT_MEMBER
    )
)
@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=ADMINISTRATOR
    )
)
async def left_event_handler(event: ChatMemberUpdated, chat_ids_with_players: Dict[str, List[str]], chat_ids_with_adm: dict):
    print(event.new_chat_member.user.id)
    print(chat_ids_with_adm[event.chat.id])
    chat_ids_with_adm[event.chat.id].remove(event.new_chat_member.user.id)

    if event.chat.id in chat_ids_with_players:
        if event.new_chat_member.user.id in chat_ids_with_players[event.chat.id]:
            chat_ids_with_players.pop(event.new_chat_member.user.id)

    await event.answer(text="THE admin is left")





@router.chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=
        (IS_ADMIN)
        >>
        IS_MEMBER
    )
)
@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=ADMINISTRATOR
    )
)
async def left_event_handler(event: ChatMemberUpdated, chat_ids_with_players: Dict[str, List[str]], chat_ids_with_adm: dict):
    print(event.new_chat_member.user.id)
    print(chat_ids_with_adm[event.chat.id])
    chat_ids_with_adm[event.chat.id].remove(event.new_chat_member.user.id)


    await event.answer(text="THE admin status was loosed")





@router.chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=
        (IS_MEMBER)
        >>
        IS_NOT_MEMBER
    )
)
@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=ADMINISTRATOR
    )
)
async def left_event_handler(event: ChatMemberUpdated, chat_ids_with_players: dict):
    

    if event.chat.id in chat_ids_with_players:
        if event.new_chat_member.user.id in chat_ids_with_players[event.chat.id]:
            chat_ids_with_players.pop(event.new_chat_member.user.id)
    
    await event.answer(text="THE member is left")
