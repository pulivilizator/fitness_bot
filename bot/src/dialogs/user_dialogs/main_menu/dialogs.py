from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Next, Button, Radio, Column, Row, Back, Start
from aiogram_dialog.widgets.text import Const, Format

from bot.src.states import MainMenuSG, SubtractCaloriesSG, PlusCaloriesSG, ChangeDataSG
from .getters import main_menu_getter

menu_dialog = Dialog(
    Window(
        Format('{main_menu_message}'),
        Row(
            Start(
                text=Format('{subtract_calories}'),
                id='subtract_calories',
                state=SubtractCaloriesSG.substract
            ),
            Start(
                text=Format('{plus_calories}'),
                id='plus_calories',
                state=PlusCaloriesSG.plus
            ),
        ),
        Start(
          text=Format('{change_data_button}'),
          id='change_data_button',
          state=ChangeDataSG.start_change_data
        ),
        state=MainMenuSG.main_menu,
        getter=main_menu_getter
    )
)

