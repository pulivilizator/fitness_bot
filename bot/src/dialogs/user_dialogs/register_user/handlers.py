from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput
from aiogram_dialog.widgets.kbd import ManagedRadio, Button
from fluentogram import TranslatorRunner

from typing import TYPE_CHECKING

from bot.src.dialogs.user_dialogs.register_user.services import create_final_user_data
from bot.src.states import MainMenuSG
from bot.src.services import UserCache, UserCacheKeys

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


async def error_parameters_handler(message: Message,
                                   widget: ManagedTextInput | MessageInput,
                                   dialog_manager: DialogManager,
                                   err: Exception | None = None):
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    bot: Bot = dialog_manager.middleware_data['bot']

    messages = {
        'weight': i18n.weight.err.message(),
        'height': i18n.height.err.message(),
        'age': i18n.age.err.message()
    }

    if err:
        await message.answer(messages[str(err)])
    else:
        await message.answer(i18n.parameters.err.message())

    await bot.delete_messages(chat_id=message.chat.id,
                              message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])


async def change_lang_handler(callback: CallbackQuery,
                              widget: ManagedRadio,
                              dialog_manager: DialogManager,
                              item_id: str):
    cache: UserCache = dialog_manager.middleware_data.get('cache')

    await cache.set_data(user_id=callback.from_user.id, key=UserCacheKeys.Settings.language(), value=item_id)


async def register_finish_handler(callback: CallbackQuery,
                                  widget: Button,
                                  dialog_manager: DialogManager):
    result_data: dict = dialog_manager.middleware_data.get('aiogd_context').widget_data
    cache: UserCache = dialog_manager.middleware_data.get('cache')

    user_data = create_final_user_data(result_data=result_data, dialog_manager=dialog_manager)

    await cache.set_data(user_id=callback.from_user.id, mapping_values=user_data)

    await dialog_manager.done()
    await dialog_manager.start(state=MainMenuSG.main_menu)


async def set_user_language(_, dialog_manager: DialogManager):
    cache: UserCache = dialog_manager.middleware_data.get('cache')
    lang = await cache.get_value(dialog_manager.event.from_user.id, UserCacheKeys.Settings.language())
    radio_lang_widget: ManagedRadio = dialog_manager.find(UserCacheKeys.Settings.language(key_to_id=True))
    await radio_lang_widget.set_checked(lang)
