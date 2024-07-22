from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Format

from bot.src.data_stores import CacheKeys
from bot.src.filters import calories_check
from bot.src.handlers.user_parameter_handlers import incorrect_message_handler, incorrect_text_handler
from bot.src.states import PlusCaloriesSG

from .getters import plus_getter
from .handlers import plus_correct_calories_handler


plus_calories_dialog = Dialog(
    Window(
        Format('{plus_calories_correctly_message}'),
        TextInput(
            id=CacheKeys.Calories.maximum_quantity(key_to_id=True),
            type_factory=calories_check,
            on_success=plus_correct_calories_handler,
            on_error=incorrect_text_handler
        ),
        MessageInput(
            func=incorrect_message_handler,
            content_types=ContentType.ANY
        ),
        Cancel(Format('{previous_button}')),
        state=PlusCaloriesSG.plus,
        getter=plus_getter
    )
)