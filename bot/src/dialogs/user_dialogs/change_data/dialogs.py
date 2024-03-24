from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format

from bot.src.states import ChangeDataSG

change_data_dialog = Dialog(
    Window(
        Format('change_data'),
        state=ChangeDataSG.start_change_data
    )
)