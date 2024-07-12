from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.fsm.state import default_state, any_state
from aiogram.filters import Command, CommandObject


router = Router()
router.my_chat_member.filter(F.chat.type == "private")
router.message.filter(F.chat.type == "private")

@router.message(Command("start") )
async def cmd_start(message: Message):
    await message.answer(text=f"Randomizer bot works in groups only\n"
                               "To make the event in the group, add me there\n"
                               "FYI, i work correctly and completely, when i am attached as admin\n"
                               "Have a nice day")
