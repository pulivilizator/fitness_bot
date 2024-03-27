from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Cancel, SwitchTo
from aiogram_dialog.widgets.text import Format

from bot.src.states import ChangeDataSG

from .getters import get_common_text, change_data_menu_getter, change_data_sex_getter

change_data_dialog = Dialog(
    Window(
        Format('{change_data_menu_message}'),
        SwitchTo(text=Format('{change_data_sex_button}'), state=ChangeDataSG.change_data_sex, id='change_data_sex'),


        Cancel(Format('{previous_button}'), id='previous'),
        state=ChangeDataSG.change_data_menu,
        getter=change_data_menu_getter
    ),

    Window(
        Format('{change_data_sex_message}'),
        state=ChangeDataSG.change_data_sex,
        getter=change_data_sex_getter
    ),
    getter=get_common_text
)
