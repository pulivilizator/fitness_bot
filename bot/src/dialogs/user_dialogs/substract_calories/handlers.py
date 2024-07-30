from aiogram import Bot
from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from sqlalchemy.ext.asyncio import AsyncSession

from bot.src.data_stores import Cache, CacheKeys
from bot.src.data_stores.db.models.user.queries import update_user_data


async def subtract_correct_calories_handler(message: Message,
                                            widget: ManagedTextInput,
                                            dialog_manager: DialogManager,
                                            text: str):
    cache: Cache = dialog_manager.middleware_data.get('cache')
    bot: Bot = dialog_manager.middleware_data['bot']
    session: AsyncSession = dialog_manager.middleware_data.get('session')
    user_id = message.from_user.id
    calories = await cache.get_value(user_id=user_id, key=CacheKeys.Calories.current_quantity())
    new_calories_value = calories - int(text)
    if new_calories_value < 0:
        new_calories_value = 0
    await update_user_data(session=session,
                           user_id=user_id,
                           user_data={CacheKeys.Calories.current_quantity(): new_calories_value})
    await cache.set_data(
        user_id=user_id,
        key=CacheKeys.Calories.current_quantity(),
        value=new_calories_value
    )

    await dialog_manager.done()
    await bot.delete_messages(chat_id=message.chat.id,
                              message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])
