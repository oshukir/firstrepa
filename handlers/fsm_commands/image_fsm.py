from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import OrganiseEvent
from aiogram.filters import ChatMemberUpdatedFilter, ADMINISTRATOR


router = Router()

router.chat_member.filter(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR))


@router.message(F.photo, OrganiseEvent.set_image)
async def download_photo(message: Message, bot: Bot, state: FSMContext, chat_ids_with_lottery):
    await bot.download(
        message.photo[-1],
        destination=f"C:/Users/ACER/Desktop/telegram_bots/frepa/photos/{message.photo[-1].file_id}.jpg"
    )
    await state.update_data(image=message.photo[-1].file_id)
    data = await state.get_data()

    chat_ids_with_lottery[message.chat.id] = {
        "name": data["name"],
        "description": data["description"],
        "prize" : data["prize"],
        "date" : data["date"],
        "time" : data["time"],
        "image_id" : data["image"]
    }
    print(chat_ids_with_lottery[message.chat.id])
    await state.clear()

    

    


@router.message(OrganiseEvent.set_name)
async def name_fsm_handler(message: Message, state: FSMContext):

    await message.answer("Please, upload a photo")