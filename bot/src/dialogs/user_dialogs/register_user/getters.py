import asyncio
from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from bot.src.db import CacheKeys
from bot.src.services.calories import counting_calories
from bot.src.services.user_data_getters import get_user_data
from bot.src.services import Language, ActiveLevel, Sex

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def get_active_levels(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, tuple | str]:
    return {
        'activity_levels': (
            (ActiveLevel.HIGH.value, i18n.activity.level.high()),
            (ActiveLevel.MEDIUM.value, i18n.activity.level.medium()),
            (ActiveLevel.LOW.value, i18n.activity.level.low()),
        ),
        'activity_message': i18n.activity.message(),
    }


async def get_lang_and_hello(dialog_manager: DialogManager,
                             i18n: TranslatorRunner,
                             **kwargs) -> dict[str, tuple | str]:
    return {
        'languages': (
            (Language.RU.value, i18n.lang.ru()),
            (Language.EN.value, i18n.lang.en())
        ),
        'hello_message': i18n.hello.message(),
        'hello_register': i18n.hello.register()
    }


async def get_geo(dialog_manager: DialogManager,
                  i18n: TranslatorRunner,
                  **kwargs) -> dict[str, tuple | str]:
    return {
        'geo_message': i18n.geo.message()
    }


async def get_sexes(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, tuple | str]:
    return {'sexes':
        (
            (Sex.MALE.value, i18n.sex.man.button()), (Sex.FEMALE.value, i18n.sex.wooman.button())
        ),
        'sex_message': i18n.sex.message(),
    }


async def get_weight(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, str]:
    return {
        'weight_message': i18n.weight.correctly.message(),
    }


async def get_height(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, str]:
    return {
        'height_message': i18n.height.correctly.message(),
    }


async def get_age(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, str]:
    return {
        'age_message': i18n.age.correctly.message(),
    }


async def get_register_finish(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, str]:
    dialog_data = dialog_manager.middleware_data.get('aiogd_context').widget_data
    calories = counting_calories(dialog_data, user_keys_id=True)
    calories_exists = 1 if calories else 0
    dialog_manager.dialog_data['max_calories'] = calories if calories else ''
    dialog_manager.dialog_data['current_calories'] = '0'
    user_data = await asyncio.to_thread(get_user_data, i18n=i18n, data=dialog_data, user_keys_id=True)
    timezone = dialog_manager.dialog_data.get(CacheKeys.Settings.timezone(key_to_id=True)) or i18n.defautl.timezone()
    return {
        'register_finish_message': i18n.register.finish.message(
            sex=user_data['sex'],
            age=user_data['age'],
            height=user_data['height'],
            weight=user_data['weight'],
            activity=user_data['activity'],
            lang=user_data['lang'],
            timezone=timezone,
            calories=calories,
            calories_exists=calories_exists
        ),
        'register_finish_button': i18n.register.finish.button(),
    }


async def get_common_text(dialog_manager: DialogManager,
                          i18n: TranslatorRunner,
                          **kwargs) -> dict[str, tuple | str]:
    return {
        'next': i18n.next.button(),
        'previous': i18n.previous.button()
    }
