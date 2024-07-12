from aiogram.filters import BaseFilter
from aiogram.types import Message

class CheckAdmin(BaseFilter):
    def __init__(self, admins: dict):
        self.admins = admins
    
    def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins[message.chat.id]