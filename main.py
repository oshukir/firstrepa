import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from config_reader import config

from handlers.usual_commands_for_start.group import (
    router as group_router
)
from handlers.usual_commands_for_start.private import (
    router as private_router
)
from handlers.usual_commands_after_start import router as after_start_router
from handlers.left_member import router as left_router
from handlers.joined_member import router as joined_router

chat_ids_with_adm = {}
chat_ids_with_players={}


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
        joined_router
    )
    
    
    await dp.start_polling(bot, allowed_updates=["message", "inline_query", "my_chat_member", "chat_member"], chat_ids_with_adm=chat_ids_with_adm,
                           chat_ids_with_players=chat_ids_with_players)

if __name__ == "__main__":
    asyncio.run(main())