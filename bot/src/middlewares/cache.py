from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User as TgUser
from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from bot.src.data_stores.db.models import User
from bot.src.data_stores.db.models.user.queries import get_user_data
from bot.src.utils.enums import UserStatus, RecountCalories
from bot.src.data_stores import Cache, CacheKeys


class CacheMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any]
    ) -> Any:
        user: TgUser = data.get('event_from_user')

        if user is None:
            return await handler(event, data)
        cache: Cache = data['cache']
        session: AsyncSession = data['session']
        user_id = user.id
        if not await cache.user_exists(user_id):
            result = await session.execute(select(exists().where(user_id == User.telegram_id)))
            user_exists = result.scalar()
            if user_exists:
                user_data = await get_user_data(session=session, user_id=user_id)
            else:
                user_data = {
                             CacheKeys.Settings.language(): user.language_code,
                             CacheKeys.status(): UserStatus.NEW,
                             CacheKeys.Settings.automatic_calorie_counting(): RecountCalories.ON
                            }

            await cache.set_data(user_id=user_id,
                                 mapping_values=user_data)

        return await handler(event, data)
