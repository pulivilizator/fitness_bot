from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import User, TelegramObject
from fluentogram import TranslatorHub

from ..services import UserCache, UserCacheKeys


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any]
    ) -> Any:
        user: User = data.get('event_from_user')

        if user is None:
            return await handler(event, data)

        cache: UserCache = data.get('cache')
        hub: TranslatorHub = data.get('hub')

        lang = await self._get_lang(event, user, cache)

        data['i18n'] = hub.get_translator_by_locale(lang or 'en')
        return await handler(event, data)

    @staticmethod
    async def _get_lang(event: TelegramObject, user: User, cache: UserCache) -> str:
        if event.callback_query and UserCacheKeys.Settings.language(key_to_id=True) in event.callback_query.data:
            return event.callback_query.data.split(':')[1]

        return await cache.get_value(user.id, UserCacheKeys.Settings.language())
