from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format

from bot.src.states import SubtractCaloriesSG

substract_calories_dialog = Dialog(
    Window(
        Format('substract'),
        state=SubtractCaloriesSG.substract
    )
)