from .register_user import register_dialog
from .main_menu import menu_dialog
from .plus_calories import plus_calories_dialog
from .substract_calories import subtract_calories_dialog
from .change_data import change_data_dialog
from .settings import settings_dialog


def get_user_dialog_routers():
    return [register_dialog, menu_dialog, plus_calories_dialog, subtract_calories_dialog, change_data_dialog,
            settings_dialog]
