from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format

from bot.src.states import PlusCaloriesSG

plus_calories_dialog = Dialog(
    Window(
        Format('plus'),
        state=PlusCaloriesSG.plus
    )
)