import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import BotCommand
from config_reader import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from middlewares import SchedulerMiddleware
from tzlocal import get_localzone

from handlers.usual_commands_for_start.group import (
    router as group_router
)
from handlers.usual_commands_for_start.private import (
    router as private_router
)
from handlers.usual_commands_after_start import router as after_start_router
from handlers.left_member import router as left_router
from handlers.joined_member import router as joined_router
from callback import router as cb_router
from handlers.fsm_commands import (
    name_fsm, description_fsm, prize_fsm, date_fsm, time_fsm, image_fsm
)

chat_ids_with_adm = {}
chat_ids_with_players={}
chat_ids_with_lottery={}
pinned_message = ""


async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Start organizing a new lottery (admins only). 🎉'),
        BotCommand(command='/cancel',
                   description='Cancel the process of creating a lottery (admins only). 🚫'),
        BotCommand(command='/delete',
                   description='Delete the existing lottery (admins only). ❌'),
        BotCommand(command='/time_left',
                   description='Check the time remaining until the lottery deadline (for all members). ⏳'),
        BotCommand(command='/participants_number',
                   description='Check the number of participants in the lottery (for all members). 🧑‍🤝‍🧑')
    ]

    await bot.set_my_commands(main_menu_commands)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher()
    bot = Bot(
        config.bot_token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp.include_routers(
        group_router,
        private_router,
        after_start_router,
        left_router,
        joined_router,
        cb_router,
        name_fsm.router,
        description_fsm.router,
        prize_fsm.router,
        date_fsm.router,
        time_fsm.router,
        image_fsm.router
    )
    scheduler = AsyncIOScheduler(timezone=get_localzone())
    dp.update.middleware.register(SchedulerMiddleware(scheduler=scheduler))
    dp.startup.register(set_main_menu)
    scheduler.start()
    
    
    await dp.start_polling(bot, allowed_updates=["message", "inline_query", "my_chat_member", "chat_member", "callback_query"], chat_ids_with_adm=chat_ids_with_adm,
                           chat_ids_with_players=chat_ids_with_players, chat_ids_with_lottery=chat_ids_with_lottery, pinned_message = pinned_message)

if __name__ == "__main__":
    asyncio.run(main())