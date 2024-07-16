from aiogram.filters import BaseFilter
from aiogram.types import Message
from typing import Tuple, List, Union, Any, Dict
from datetime import datetime
from datetime import date as datef
from aiogram import Bot

class CheckAdmin(BaseFilter):
    def __init__(self, admins: dict):
        self.admins = admins
    
    def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins[message.chat.id]
    

class CheckDateFormat(BaseFilter):

  async def __call__(self, message: Message) -> Union[bool, None]:
    try:
            date_text = message.text
            print(f"Received date: {date_text}")
            date_format = "%d/%m/%Y"

            parsed_date = datetime.strptime(date_text, date_format)

            day, month, year = parsed_date.day, parsed_date.month, parsed_date.year
            print("THE TEMPLATE IS PASSED")

            today = datetime.now()
            future_date = datetime(year, month, day)
            
            print(f"Today's date and time: {today}")
            print(f"Future date and time: {future_date}")
            print(f"{year} and {type(year)}")
            print(f"{month} and {type(month)}")
            print(f"{day} and {type(day)}")


            if (today.day <= future_date.day and today.month <= future_date.month and today.year <= future_date.year):
                print("THE DATE IS SET FOR A FUTURE EVENT")
                return {"date": [year, month, day]}
            else:
                print("THE DATE IS IN THE PAST")
                return {"date": ["error"]}

    except ValueError as e:
            print(f"DATE FORMAT ERROR: {e}")
            return {"date": ["error"]}


    

class CheckTimeFormat(BaseFilter):
  async def __call__(self, message: Message) ->  Union[bool, Dict[str, Any]]:
    try:
        time = message.text

        format = "%H:%M"
        parsed_date = datetime.strptime(time, format)

        hour, minute = parsed_date.hour, parsed_date.minute

        return {"time" : [hour, minute]}
    except ValueError:
        return False 
    

class AdminFilter(BaseFilter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        chat_member = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        if chat_member.status in ("administrator", "creator"):
    # The user is an admin, handle accordingly
            return True
        else:
    # The user is not an admin
            return False