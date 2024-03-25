from typing import TYPE_CHECKING, Literal
from bot.src.utils import Language, ActiveLevel, Sex, UserKeys

from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


def _get_user_data(i18n: TranslatorRunner, data: dict, user_keys_id=False) -> dict:
    return {
        'sex': sex_determining(
            sex=data.get(UserKeys.UserData.gender(key_to_id=user_keys_id)),
            i18n=i18n),
        'age': data.get(UserKeys.UserData.age(key_to_id=user_keys_id)) or i18n.defautl.parameter(),
        'height': data.get(UserKeys.UserData.height(key_to_id=user_keys_id)) or i18n.defautl.parameter(),
        'weight': data.get(UserKeys.UserData.weight(key_to_id=user_keys_id)) or i18n.defautl.parameter(),
        'max_calories': data.get(UserKeys.Calories.maximum_quantity(key_to_id=user_keys_id)) or i18n.defautl.parameter(),
        'current_calories': data.get(UserKeys.Calories.current_quantity(key_to_id=user_keys_id)),
        'lang': lang_determining(
            lang=data.get(UserKeys.UserData.language(key_to_id=user_keys_id)),
            i18n=i18n
        ),
        'activity': activity_determining(
            activity=data.get(UserKeys.UserData.activity(key_to_id=user_keys_id)),
            i18n=i18n)
    }


def activity_determining(activity: ActiveLevel, i18n: TranslatorRunner) -> str:
    match activity:
        case ActiveLevel.HIGH.value:
            return i18n.activity.level.high()
        case ActiveLevel.MEDIUM.value:
            return i18n.activity.level.medium()
        case ActiveLevel.LOW.value:
            return i18n.activity.level.low()
        case _:
            return i18n.defautl.parameter()


def sex_determining(sex: Sex, i18n: TranslatorRunner) -> str:
    match sex:
        case Sex.MALE.value:
            return i18n.sex.man.button()
        case Sex.FEMALE.value:
            return i18n.sex.wooman.button()
        case _:
            return i18n.defautl.parameter()


def lang_determining(lang: Language, i18n: TranslatorRunner) -> str:
    match lang:
        case Language.RU.value:
            return i18n.lang.ru()
        case Language.EN.value:
            return i18n.lang.en()
        case _:
            return i18n.defautl.parameter()
