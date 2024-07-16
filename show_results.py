from aiogram import types, html
from typing import Dict, Any
from aiogram.types import FSInputFile
from datetime import datetime
from aiogram.enums.parse_mode import ParseMode
from keyboards.inline_keyboard import get_participate_keyboard


async def demonstrate(message: types.Message, data):
    name = data["name"]
    description = data["description"]
    prize = data["prize"]
    date_list = data["date"]
    time_list = data["time"]
    image_id = data["image_id"]

    final_date = datetime(date_list[0], date_list[1], date_list[2], time_list[0], time_list[1])
    
    text = (
        f"🎉🎉🎉 {name} 🎉🎉🎉\n\n"
        f"🔔 {html.bold('Description:')} 🔔\n"
        f"{description}\n\n"
        f"💰💰💰 {html.bold('Prize fund:')} 💰💰💰\n"
        f"{prize}\n\n"
        f"⏳ {html.bold('Results day:')} ⏳\n"
        f"{final_date.strftime('%d %B %Y')} в {final_date.strftime('%H:%M')}\n\n"
        f"🔥 Don't miss your chance to become a winner! 🔥\n"
        f"🍀🌟 Participate right now and win! 🌟🍀"
    )
    
    image_from_pc = FSInputFile(f"C:/Users/ACER/Desktop/telegram_bots/frepa/photos/{image_id}.jpg")

    return await message.answer_photo(
        image_from_pc,
        caption=text,
        parse_mode=ParseMode.HTML,
        reply_markup=get_participate_keyboard()
    )