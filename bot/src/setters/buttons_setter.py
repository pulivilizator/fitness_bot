import asyncio
from typing import Callable, Any

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import ManagedWidget

from bot.src.data_stores import Cache


class SetButtonChecked:
    def __init__(self, *keys: Callable):
        self._keys = keys

    async def __call__(self, _: Any, dialog_manager: DialogManager):
        print()
        await self._set_default_buttons(_, dialog_manager=dialog_manager, keys=self._keys)

    async def _set_checked(self, cache: Cache, dialog_manager: DialogManager, cache_key: Callable):
        user_value = await cache.get_value(
            user_id=dialog_manager.event.from_user.id, key=cache_key())
        widget: ManagedWidget = dialog_manager.find(cache_key(key_to_id=True))
        await widget.set_checked(user_value)

    async def _set_default_buttons(self, _, dialog_manager: DialogManager, keys):
        cache: Cache = dialog_manager.middleware_data.get('cache')
        await asyncio.gather(
            *[
                asyncio.create_task(self._set_checked(cache, dialog_manager, cache_key))
                for cache_key in keys
            ]
        )
