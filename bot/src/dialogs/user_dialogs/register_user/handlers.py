from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import ManagedRadio, Button

from typing import TYPE_CHECKING

from bot.src.dialogs.user_dialogs.register_user.services import create_final_user_data
from bot.src.services.timezone import update_dialog_data
from bot.src.states import MainMenuSG
from bot.src.db import Cache, CacheKeys

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def correct_parameters_handler(message: Message,
                                     widget: ManagedTextInput,
                                     dialog_manager: DialogManager,
                                     text: str):
    await dialog_manager.next()
    bot: Bot = dialog_manager.middleware_data['bot']
    await bot.delete_messages(chat_id=message.chat.id,
                              message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])


async def change_lang_handler(callback: CallbackQuery,
                              widget: ManagedRadio,
                              dialog_manager: DialogManager,
                              item_id: str):
    cache: Cache = dialog_manager.middleware_data.get('cache')

    await cache.set_data(user_id=callback.from_user.id, key=CacheKeys.Settings.language(), value=item_id)


async def correct_geo_handler(message: Message,
                              widget: ManagedTextInput,
                              dialog_manager: DialogManager,
                              text: str):
    try:
        await update_dialog_data(dialog_manager, text)
    except ValueError:
        i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
        await message.answer(i18n.geo.err.message())
    else:
        await dialog_manager.next()
    finally:
        bot: Bot = dialog_manager.middleware_data['bot']
        await bot.delete_messages(chat_id=message.chat.id,
                                  message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])


async def register_finish_handler(callback: CallbackQuery,
                                  widget: Button,
                                  dialog_manager: DialogManager):
    result_data: dict = dialog_manager.middleware_data.get('aiogd_context').widget_data
    cache: Cache = dialog_manager.middleware_data.get('cache')

    user_data = create_final_user_data(result_data=result_data, dialog_manager=dialog_manager)

    await cache.set_data(user_id=callback.from_user.id, mapping_values=user_data)

    await dialog_manager.done()
    await dialog_manager.start(state=MainMenuSG.main_menu)
