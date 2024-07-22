from aiogram import Bot
from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

from bot.src.data_stores import Cache, CacheKeys


async def plus_correct_calories_handler(message: Message,
                                               widget: ManagedTextInput,
                                               dialog_manager: DialogManager,
                                               text: str):
    cache: Cache = dialog_manager.middleware_data.get('cache')
    bot: Bot = dialog_manager.middleware_data['bot']
    user_id = message.from_user.id
    calories = await cache.get_value(user_id=user_id, key=CacheKeys.Calories.current_quantity())
    new_calories_value = calories + int(text)
    await cache.set_data(
        user_id=user_id,
        key=CacheKeys.Calories.current_quantity(),
        value=new_calories_value
    )

    await dialog_manager.done()
    await bot.delete_messages(chat_id=message.chat.id,
                              message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])