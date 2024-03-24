from typing import TYPE_CHECKING, Optional

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from bot.src.utils import Language, ActiveLevel, Sex, UserKeys

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def get_active_levels(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, tuple | str]:
    return {
        'active_levels': (
            (ActiveLevel.HIGH.value, i18n.activity.level.high()),
            (ActiveLevel.MEDIUM.value, i18n.activity.level.medium()),
            (ActiveLevel.LOW.value, i18n.activity.level.low()),
        ),
        'activity_message': i18n.activity.message(),
        'next': i18n.next.button(),
        'previous': i18n.previous.button()
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


async def get_sexes(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, tuple | str]:
    return {'sexes':
        (
            (Sex.MALE.value, i18n.sex.man.button()), (Sex.FEMALE.value, i18n.sex.wooman.button())
        ),
        'sex_message': i18n.sex.message(),
        'next': i18n.next.button(),
        'previous': i18n.previous.button()
    }


async def get_weight(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, str]:
    return {
        'weight_message': i18n.weight.correctly.message(),
        'next': i18n.next.button(),
        'previous': i18n.previous.button()
    }


async def get_height(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, str]:
    return {
        'height_message': i18n.height.correctly.message(),
        'next': i18n.next.button(),
        'previous': i18n.previous.button()
    }


async def get_age(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, str]:
    return {
        'age_message': i18n.age.correctly.message(),
        'next': i18n.next.button(),
        'previous': i18n.previous.button()
    }


async def get_register_finish(dialog_manager: DialogManager, i18n: TranslatorRunner, **kwargs) -> dict[str, str]:
    dialog_data = dialog_manager.middleware_data.get('aiogd_context').widget_data
    calories = _counting_calories(dialog_data)
    calories_exists = 1 if calories else 0
    dialog_manager.dialog_data['calories'] = calories if calories else ''
    user_data = _get_user_data(i18n, dialog_data)
    return {
        'register_finish_message': i18n.register.finish.message(
            sex=user_data['sex'],
            age=user_data['age'],
            height=user_data['height'],
            weight=user_data['weight'],
            activity=user_data['activity'],
            lang=user_data['lang'],
            calories=calories,
            calories_exists=calories_exists
        ),
        'register_finish_button': i18n.register.finish.button(),
        'previous': i18n.previous.button(),
    }


def _get_user_data(i18n: TranslatorRunner, dialog_data: dict):
    user_data = {}
    match dialog_data.get(UserKeys.Settings.gender.__str__(id=True)):
        case Sex.MALE.value:
            user_data['sex'] = i18n.sex.man.button()
        case Sex.FEMALE.value:
            user_data['sex'] = i18n.sex.wooman.button()
        case _:
            user_data['sex'] = i18n.defautl.parameter()

    user_data['age'] = dialog_data.get(UserKeys.Settings.age.__str__(id=True)) or i18n.defautl.parameter()
    user_data['height'] = dialog_data.get(UserKeys.Settings.height.__str__(id=True)) or i18n.defautl.parameter()
    user_data['weight'] = dialog_data.get(UserKeys.Settings.weight.__str__(id=True)) or i18n.defautl.parameter()

    match dialog_data.get(UserKeys.Settings.language.__str__(id=True)):
        case Language.RU.value: user_data['lang'] = i18n.lang.ru()
        case Language.EN.value: user_data['lang'] = i18n.lang.en()
        case _: user_data['lang'] = i18n.defautl.parameter()

    match dialog_data.get(UserKeys.Settings.activity.__str__(id=True)):
        case ActiveLevel.HIGH.value:
            user_data['activity'] = i18n.activity.level.high()
        case ActiveLevel.MEDIUM.value:
            user_data['activity'] = i18n.activity.level.medium()
        case ActiveLevel.LOW.value:
            user_data['activity'] = i18n.activity.level.low()
        case _:
            user_data['activity'] = i18n.defautl.parameter()

    return user_data


def _get_active_multiplier(active: str) -> float:
    match active:
        case ActiveLevel.HIGH.value:
            return 1.5
        case ActiveLevel.MEDIUM.value:
            return 1.3
        case ActiveLevel.LOW.value:
            return 1.1
        case _:
            return 1


def _counting_calories(user_data: dict) -> Optional[int]:
    multiplier = _get_active_multiplier(user_data.get(UserKeys.Settings.activity.__str__(id=True)))
    try:
        sex = user_data.get(UserKeys.Settings.gender.__str__(id=True))
        age = int(user_data.get(UserKeys.Settings.age.__str__(id=True)))
        height = int(user_data.get(UserKeys.Settings.height.__str__(id=True)))
        weight = int(user_data.get(UserKeys.Settings.weight.__str__(id=True)))
    except TypeError:
        return
    if sex == Sex.MALE.value:
        return int(((height * 5) - (age * 6.8) + (weight * 13.7) + 66) * multiplier)
    elif sex == Sex.FEMALE.value:
        return int(((height * 1.8) - (age * 4.7) + (weight * 9.6) + 665) * multiplier)
