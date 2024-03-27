from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def change_data_menu_getter(dialog_manager: DialogManager,
                                  i18n: TranslatorRunner,
                                  **kwargs) -> dict[str, tuple | str]:
    return {
        'change_data_menu_message': i18n.change.data.menu.message(),
        'change_data_sex_button': i18n.change.data.sex.button(),
    }


async def change_data_sex_getter(dialog_manager: DialogManager,
                                 i18n: TranslatorRunner,
                                 **kwargs) -> dict[str, tuple | str]:
    return {
        'change_data_sex_message': i18n.change.data.sex.message(),
    }


async def get_common_text(dialog_manager: DialogManager,
                          i18n: TranslatorRunner,
                          **kwargs) -> dict[str, tuple | str]:
    return {
        'previous_button': i18n.previous.button()
    }
