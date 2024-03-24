from .user_dialogs import get_user_dialog_routers
from .admin_dialogs import get_admin_dialog_routers


def get_dialog_routers():
    return [*get_admin_dialog_routers(), *get_user_dialog_routers()]