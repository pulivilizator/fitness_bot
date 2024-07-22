from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from typing import TYPE_CHECKING

from bot.src.utils.enums import Language

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def get_langs(dialog_manager: DialogManager,
                    i18n: TranslatorRunner,
                    **kwargs) -> dict[str, tuple | str]:
    return {
        'languages': (
            (Language.RU.value, i18n.lang.ru()),
            (Language.EN.value, i18n.lang.en())
        ),
        'change_language_message': i18n.language.change.message()
    }


async def settings_menu_getter(dialog_manager: DialogManager,
                               i18n: TranslatorRunner,
                               **kwargs) -> dict[str, tuple | str]:
    return {
        'settings_message': i18n.settings.message(),
        'change_language_button': i18n.language.change.button(),
        'calories_counting_on': i18n.calories.counting.on(),
        'calories_counting_off': i18n.calories.counting.off()
    }


async def get_common_text(dialog_manager: DialogManager,
                          i18n: TranslatorRunner,
                          **kwargs) -> dict[str, tuple | str]:
    return {
        'previous_button': i18n.previous.button()
    }
