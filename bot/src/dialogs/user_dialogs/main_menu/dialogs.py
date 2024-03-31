from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Start
from aiogram_dialog.widgets.text import Format

from bot.src.states import MainMenuSG, SubtractCaloriesSG, PlusCaloriesSG, ChangeDataSG, SettingsSG
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
          state=ChangeDataSG.change_data_menu
        ),
        Start(
            text=Format('{settings_button}'),
            id='settings_button',
            state=SettingsSG.settings_menu
        ),
        state=MainMenuSG.main_menu,
        getter=main_menu_getter
    )
)

