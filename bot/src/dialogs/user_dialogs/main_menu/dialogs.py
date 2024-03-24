from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Next, Button, Radio, Column, Row, Back
from aiogram_dialog.widgets.text import Const, Format

from bot.src.states import MainMenuSg


menu_dialog = Dialog(
    Window(
        Format('qwe'),
        state=MainMenuSg.main_menu
    )
)