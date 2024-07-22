import asyncio

from aiogram import html
from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from typing import TYPE_CHECKING

from bot.src.data_stores import Cache
from bot.src.services.user_data_getters import get_user_data

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def main_menu_getter(dialog_manager: DialogManager,
                           i18n: TranslatorRunner,
                           event_from_user: User,
                           cache: Cache,
                           **kwargs):
    username = html.quote(event_from_user.full_name or event_from_user.username)
    user_cache_data = await cache.get_all_data(event_from_user.id)
    user_data = await asyncio.to_thread(get_user_data, i18n=i18n, data=user_cache_data)
    return {
        'main_menu_message': i18n.main.menu.message(
            username=username,
            sex=user_data['sex'],
            age=user_data['age'],
            activity=user_data['activity'],
            weight=user_data['weight'],
            height=user_data['height'],
            lang=user_data['lang'],
            calories=user_data['max_calories'],
            current_calories=user_data['current_calories'],
            timezone=user_data['timezone']
        ),
        'subtract_calories': i18n.subtract.calories.button(),
        'plus_calories': i18n.plus.calories.button(),
        'change_data_button': i18n.change.data.button(),
        'settings_button': i18n.settings.button()
    }
