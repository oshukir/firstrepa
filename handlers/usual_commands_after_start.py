from aiogram.types import Message, ChatMemberUpdated
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.fsm.state import default_state, any_state
from aiogram.filters import Command, CommandObject, ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import (
    IS_NOT_MEMBER, IS_ADMIN, MEMBER, ADMINISTRATOR
)
from typing import Dict
from keyboards.inline_keyboard import get_keyboard
from filter import AdminFilter



router = Router()
router.my_chat_member.filter(F.chat.type.in_({"group", "supergroup"}))
router.message.filter(F.chat.type.in_({"group", "supergroup"}))
router.chat_member.filter(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR))


@router.message(
    Command("start"), default_state
)
async def cmd_start(message: Message, chat_ids_with_adm):

    print(message.chat.id)
    print(chat_ids_with_adm)

    if message.chat.id in chat_ids_with_adm and message.from_user.id in chat_ids_with_adm[message.chat.id]:
        await message.answer(text="YEEEEH, you are admin. So lets start",
                             reply_markup=get_keyboard())
    else:
        await message.answer("Organising lotteries is available only for admins")


@router.message(
    Command("cancel"), default_state, AdminFilter()
)
async def cmd_cancel(message: Message, state: FSMContext):
    await message.answer(
        text="There is nothing to cancel"
    )


@router.message(
    Command("cancel"), any_state, AdminFilter()
)
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="To start making event from a scratch press /start"
    )


@router.message(
    Command("delete"), default_state, AdminFilter()
)
async def cmd_delete(message: Message, chat_ids_with_lottery: dict):
    if len(chat_ids_with_lottery[message.chat.id]) == 0:
        await message.answer(
            text="There is no lottery to delete"
        )
    else:
        name = chat_ids_with_lottery[message.chat.id]["name"]
        await message.answer(
            text="The only event {} is deleted".format(name)
        )
        chat_ids_with_lottery[message.chat.id].clear()
        print(chat_ids_with_lottery[message.chat.id])


