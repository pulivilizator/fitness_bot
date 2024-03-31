from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from bot.src.services import Sex, ActiveLevel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def change_data_menu_getter(dialog_manager: DialogManager,
                                  i18n: TranslatorRunner,
                                  **kwargs) -> dict[str, tuple | str]:
    return {
        'change_data_menu_message': i18n.change.data.menu.message(),
        'change_data_sex_button': i18n.change.data.sex.button(),
        'change_data_activity_button': i18n.change.data.activity.button(),
        'change_data_age_button': i18n.change.data.age.button(),
        'change_data_weight_button': i18n.change.data.weight.button(),
        'change_data_height_button': i18n.change.data.height.button(),
        'change_data_calories_button': i18n.change.data.calories.button(),
        'change_data_save_update_calories': i18n.change.data.save.update.calories()
    }


async def change_data_sex_getter(dialog_manager: DialogManager,
                                 i18n: TranslatorRunner,
                                 **kwargs) -> dict[str, tuple | str]:
    return {
        'change_data_sex_message': i18n.change.data.sex.message(),
        'sexes':
            (
                (Sex.MALE.value, i18n.sex.man.button()), (Sex.FEMALE.value, i18n.sex.wooman.button())
            ),
    }


async def change_data_activity_getter(dialog_manager: DialogManager,
                                      i18n: TranslatorRunner,
                                      **kwargs) -> dict[str, tuple | str]:
    return {
        'change_data_activity_message': i18n.change.data.activity.message(),
        'activity_levels': (
            (ActiveLevel.HIGH.value, i18n.activity.level.high()),
            (ActiveLevel.MEDIUM.value, i18n.activity.level.medium()),
            (ActiveLevel.LOW.value, i18n.activity.level.low()),
        ),
    }


async def change_data_age_getter(dialog_manager: DialogManager,
                                 i18n: TranslatorRunner,
                                 **kwargs) -> dict[str, tuple | str]:
    return {
        'change_data_age_message': i18n.change.data.age.message()
    }


async def change_data_weight_getter(dialog_manager: DialogManager,
                                    i18n: TranslatorRunner,
                                    **kwargs) -> dict[str, tuple | str]:
    return {
        'change_data_weight_message': i18n.change.data.weight.message()
    }


async def change_data_height_getter(dialog_manager: DialogManager,
                                    i18n: TranslatorRunner,
                                    **kwargs) -> dict[str, tuple | str]:
    return {
        'change_data_height_message': i18n.change.data.height.message()
    }


async def change_data_calories_getter(dialog_manager: DialogManager,
                                      i18n: TranslatorRunner,
                                      **kwargs) -> dict[str, tuple | str]:
    return {
        'change_data_calories_message': i18n.change.data.calories.message()
    }


async def get_common_text(dialog_manager: DialogManager,
                          i18n: TranslatorRunner,
                          **kwargs) -> dict[str, tuple | str]:
    return {
        'previous_button': i18n.previous.button()
    }
