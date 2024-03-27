from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from ..services import UserCache, UserCacheKeys, UserStatus
from bot.src.states import UserRegisterSG, MainMenuSG

commands_router = Router()


@commands_router.message(CommandStart())
async def process_start(message: Message, dialog_manager: DialogManager, cache: UserCache):
    status = await cache.get_value(user_id=message.from_user.id, key=UserCacheKeys.status())
    await message.delete()
    if status == UserStatus.NEW.value:
        await dialog_manager.start(state=UserRegisterSG.start, mode=StartMode.RESET_STACK)
    else:
        await dialog_manager.start(state=MainMenuSG.main_menu, mode=StartMode.RESET_STACK)
