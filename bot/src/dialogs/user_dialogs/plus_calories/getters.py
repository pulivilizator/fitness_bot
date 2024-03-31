from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def plus_getter(dialog_manager: DialogManager,
                      i18n: TranslatorRunner,
                      **kwargs):
    return {
        'plus_calories_correctly_message': i18n.plus.calories.correctly.message(),
        'previous_button': i18n.previous.button()
    }
