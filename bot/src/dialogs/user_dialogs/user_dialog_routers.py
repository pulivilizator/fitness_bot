from .register_user import register_dialog
from .main_menu import menu_dialog
from .plus_calories import plus_calories_dialog
from .substract_calories import substract_calories_dialog
from .change_data import change_data_dialog


def get_user_dialog_routers():
    return [register_dialog, menu_dialog, plus_calories_dialog, substract_calories_dialog, change_data_dialog]
