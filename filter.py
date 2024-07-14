from aiogram.filters import BaseFilter
from aiogram.types import Message
from typing import Tuple, List, Union, Any, Dict
from datetime import datetime
from datetime import date as datef

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

            # Parse the date according to the specified format
            parsed_date = datetime.strptime(date_text, date_format)

            # Extract date components
            day, month, year = parsed_date.day, parsed_date.month, parsed_date.year
            print("THE TEMPLATE IS PASSED")

            today = datetime.now()
            future_date = datetime(year, month, day)
            
            print(f"Today's date and time: {today}")
            print(f"Future date and time: {future_date}")
            print(f"{year} and {type(year)}")
            print(f"{month} and {type(month)}")
            print(f"{day} and {type(day)}")

            # Check if the parsed date is in the future
            if today < future_date:
                print("THE DATE IS SET FOR A FUTURE EVENT")
                return {"date": [year, month, day]}  # Return a list for clarity
            else:
                print("THE DATE IS IN THE PAST")
                return {"date": ["error"]}

    except ValueError as e:
            print(f"DATE FORMAT ERROR: {e}")
            return {"date": ["error"]}


    

class CheckTimeFormat(BaseFilter):
  async def __call__(self, message: Message) ->  Union[bool, Dict[str, Any]]:
    try:
      date = message.text


      format = "%H:%M"
      res = datetime.strptime(date, format)

      list1 = [int(element) for element in date.split(":")]

      return {"time" : list1}
    except ValueError:
      return False  # Or raise an exception if you prefer