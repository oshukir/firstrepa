from aiogram import Router, F, html
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states import OrganiseEvent


router = Router()


@router.callback_query(F.data == "organise")
async def send_fsm(callback : CallbackQuery, chat_ids_with_adm, state: FSMContext):
    print("!!!!!!!!!!!!!!!!!!!!!INSIDE CALLBACK TRACKER!!!!!!!!!!!!!!!!!!!!!!")
    if chat_ids_with_adm[callback.message.chat.id].count(callback.from_user.id) >= 1:
        await state.set_state(OrganiseEvent.set_name)
        await callback.message.answer(
            text="As you are valid person,\n"
                 "Follow my instructions, and fill the form\n"
                 "Let's begin from name of lottery",
        )
        await callback.answer()
    else:
        await callback.answer(show_alert=True, text="You are not allowed to make event")


@router.callback_query(F.data == "participate")
async def send_fsm(callback : CallbackQuery, chat_ids_with_adm, state: FSMContext, chat_ids_with_players, chat_ids_with_lottery):
    print("!!!!!!!!!!!!!!!!!!!!!INSIDE CALLBACK TRACKER (2)!!!!!!!!!!!!!!!!!!!!!!")
    await callback.answer(
        text=f"You are in"
    )
    chat_ids_with_players[callback.message.chat.id].append(callback.from_user.id)
    