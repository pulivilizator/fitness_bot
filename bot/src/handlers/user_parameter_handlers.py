from typing import TYPE_CHECKING

from aiogram import Bot
from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput, ManagedTextInput
from fluentogram import TranslatorRunner

from bot.src.db import Cache, CacheKeys

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


async def incorrect_message_handler(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    bot: Bot = dialog_manager.middleware_data['bot']
    await message.answer(i18n.parameters.err.message())
    await bot.delete_messages(chat_id=message.chat.id,
                              message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])


async def incorrect_text_handler(message: Message,
                                 widget: ManagedTextInput | MessageInput,
                                 dialog_manager: DialogManager,
                                 err: Exception | None = None):
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    bot: Bot = dialog_manager.middleware_data['bot']

    messages = {
        'weight': i18n.weight.err.message(),
        'height': i18n.height.err.message(),
        'age': i18n.age.err.message(),
        'geo': i18n.geo.err.message(),
        'calories': i18n.plus.calories.err.message()
    }

    await message.answer(messages[str(err)])

    await bot.delete_messages(chat_id=message.chat.id,
                              message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])
