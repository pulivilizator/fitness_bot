from .handlers import commands_router
from .dialogs import get_dialog_routers

def get_routers():
    return [commands_router, *get_dialog_routers()]