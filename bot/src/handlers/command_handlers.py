from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.src.utils.enums import UserStatus
from bot.src.states import UserRegisterSG, MainMenuSG
from bot.src.data_stores import Cache, CacheKeys

commands_router = Router()


@commands_router.message(CommandStart())
async def process_start(message: Message, dialog_manager: DialogManager, cache: Cache):
    status = await cache.get_value(user_id=message.from_user.id, key=CacheKeys.status())
    await message.delete()
    if status == UserStatus.NEW.value:
        await dialog_manager.start(state=UserRegisterSG.start, mode=StartMode.RESET_STACK)
    else:
        await dialog_manager.start(state=MainMenuSG.main_menu, mode=StartMode.RESET_STACK)
