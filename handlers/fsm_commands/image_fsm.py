from show_results import demonstrate
from aiogram import Router, F, Bot, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import OrganiseEvent
from aiogram.filters import ChatMemberUpdatedFilter, ADMINISTRATOR
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from random import choice
from datetime import datetime, timedelta

router = Router()

router.chat_member.filter(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR))


async def send_message_by_schedule(bot: Bot, chat_id: str , players: list, lottery_name:str, message_id, lottery):
    if len(players) >= 1:
        winner = choice(players)
        member = await bot.get_chat_member(chat_id=chat_id, user_id=winner)
        user = member.user

        text = (
            f"🏆 {html.bold('Congratulations!')} 🏆\n"
            f"🎉 @{user.first_name}, you are the winner of the {lottery_name}! 🎉"
        )
    else:
        text = (f"🎉 No one participated! 🎉")

    lottery.clear()
    

    await bot.send_message(chat_id=chat_id, text=text, reply_to_message_id=message_id)


@router.message(F.photo, OrganiseEvent.set_image)
async def download_photo(message: Message, bot: Bot, state: FSMContext, chat_ids_with_lottery, chat_ids_with_players, pinned_message, apscheduler: AsyncIOScheduler):
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
    chat_ids_with_players[message.chat.id] = []
    await state.clear()

    print("BEFOREEE DEMONSTRATING RESULTS")
    sent_message = await demonstrate(message=message, data=chat_ids_with_lottery[message.chat.id])
    pinned_message = sent_message.message_id

    await bot.pin_chat_message(chat_id=message.chat.id, message_id=pinned_message)


    day = data["date"][2]
    month = data["date"][1]
    year = data["date"][0]
    hour = data["time"][0]
    minute = data["time"][1]

    run_date= (datetime(day=day, month = month, year = year, hour = hour, minute = minute) - datetime.now()) + datetime.now()
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!{run_date}!!!!!!!!!!!!!!!!!!!!!!!1")

    try:
        job = apscheduler.add_job(
            send_message_by_schedule,
            trigger="date",
            run_date=run_date,
            id="one_job",
            kwargs={
                'bot': bot,
                'chat_id': message.chat.id,
                'players': chat_ids_with_players[message.chat.id],
                "lottery_name": data["name"],
                'message_id' : sent_message.message_id,
                'lottery' : chat_ids_with_lottery[message.chat.id]
            }
        )
        print(f"Job added successfully: {job.id}")
    except Exception as e:
        print(f"Failed to add job: {e}")







    


@router.message(OrganiseEvent.set_name)
async def name_fsm_handler(message: Message, state: FSMContext):

    await message.answer("Please, upload a photo")