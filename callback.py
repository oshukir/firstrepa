from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states import OrganiseEvent


router = Router()

@router.callback_query(F.data == "organise")
async def send_fsm(callback : CallbackQuery, chat_ids_with_adm, state: FSMContext):
    print("!!!!!!!!!!!!!!!!!!!!!INSIDE CALLBACK TRACKER!!!!!!!!!!!!!!!!!!!!!!")
    if chat_ids_with_adm[callback.message.chat.id].count(callback.message.from_user.id):
        state.set_state(OrganiseEvent.set_name)
        await callback.message.answer(
            text="As you are valid person,\n"
                 "Follow my instructions, and fill the form"
        )
    else:
        await callback.message.answer(
            text="As you are not valid person to make event\n"
                 "You are not allowed to follow my next instructions"
        )
    await callback.answer()