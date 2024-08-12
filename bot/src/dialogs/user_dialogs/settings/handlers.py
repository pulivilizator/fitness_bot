from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedCheckbox, Button
from sqlalchemy.ext.asyncio import AsyncSession

from bot.src.data_stores import Cache, CacheKeys
from bot.src.data_stores.db.models.user.queries import update_user_data


async def settings_calories_counting_handler(callback: CallbackQuery,
                                             widget: ManagedCheckbox,
                                             dialog_manager: DialogManager):
    cache: Cache = dialog_manager.middleware_data.get('cache')
    await cache.set_data(
        user_id=callback.from_user.id,
        key=CacheKeys.Settings.automatic_calorie_counting(),
        value=widget.is_checked()
    )


async def to_menu_onclick(callback: CallbackQuery,
                          widget: Button,
                          dialog_manager: DialogManager):
    user_id = callback.from_user.id
    cache: Cache = dialog_manager.middleware_data.get('cache')
    session: AsyncSession = dialog_manager.middleware_data.get('session')
    lang = await cache.get_value(user_id=user_id, key=CacheKeys.Settings.language())
    autocounting = await cache.get_value(user_id=user_id, key=CacheKeys.Settings.automatic_calorie_counting())
    await update_user_data(session=session,
                           user_id=user_id,
                           user_data={
                               CacheKeys.Settings.language(): lang,
                               CacheKeys.Settings.automatic_calorie_counting(): bool(autocounting)
                           })
