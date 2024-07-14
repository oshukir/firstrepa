from aiogram.filters import BaseFilter
from aiogram.types import Message
from typing import Tuple, List, Union, Any, Dict
from datetime import datetime

class CheckAdmin(BaseFilter):
    def __init__(self, admins: dict):
        self.admins = admins
    
    def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins[message.chat.id]
    

class CheckDateFormat(BaseFilter):
  def __call__(self, message: Message) ->  Union[bool, Dict[str, Any]]:
    try:
      date = message.text

      format = "%d/%m/%Y"
      res = datetime.strptime(date, format)

      list1 = [int(element) for element in date.split("/")]

      return {"date" : list1}
    except ValueError:
      return False  # Or raise an exception if you prefer