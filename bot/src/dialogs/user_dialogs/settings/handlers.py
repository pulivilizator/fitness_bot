from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedCheckbox

from bot.src.db import Cache, CacheKeys


async def settings_calories_counting_handler(callback: CallbackQuery,
                                             widget: ManagedCheckbox,
                                             dialog_manager: DialogManager):
    cache: Cache = dialog_manager.middleware_data.get('cache')
    await cache.set_data(
        user_id=callback.from_user.id,
        key=CacheKeys.Settings.automatic_calorie_counting(),
        value=widget.is_checked()
    )
