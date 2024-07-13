# from typing import Any, Callable, Dict, Awaitable
# from datetime import datetime
# from aiogram import BaseMiddleware
# from aiogram.types import TelegramObject, ChatMember

# # Мидлварь, которая достаёт внутренний айди юзера из какого-то стороннего сервиса
# class CheckParticipance(BaseMiddleware):
#     # Разумеется, никакого сервиса у нас в примере нет,
#     # а только суровый рандом:

#     async def __call__(
#             self,
#             handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#             event: ChatMember,
#             data: Dict[str, Any],
#     ) -> Any:
        
#         return await handler(event, data)