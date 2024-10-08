from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput, ManagedTextInput
from aiogram_dialog.widgets.kbd import ManagedRadio, Button
from sqlalchemy.ext.asyncio import AsyncSession

from bot.src.data_stores import Cache, CacheKeys
from bot.src.data_stores.db.models.user.queries import update_user_data, get_user_data as get_db_user_data
from bot.src.states import ChangeDataSG
from bot.src.services import get_user_data, counting_calories
from bot.src.utils.enums import RecountCalories


async def change_data_sex_handler(callback: CallbackQuery,
                                  widget: ManagedRadio,
                                  dialog_manager: DialogManager,
                                  item_id: str):
    if item_id == 'None':
        return
    cache: Cache = dialog_manager.middleware_data.get('cache')
    await cache.set_data(
        user_id=callback.from_user.id,
        key=CacheKeys.UserData.gender(),
        value=item_id
    )


async def change_data_activity_handler(callback: CallbackQuery,
                                       widget: ManagedRadio,
                                       dialog_manager: DialogManager,
                                       item_id: str):
    if item_id == 'None':
        return
    cache: Cache = dialog_manager.middleware_data.get('cache')
    await cache.set_data(
        user_id=callback.from_user.id,
        key=CacheKeys.UserData.activity(),
        value=item_id
    )


async def change_data_correct_age_handler(message: Message,
                                          widget: ManagedTextInput,
                                          dialog_manager: DialogManager,
                                          text: str):
    cache: Cache = dialog_manager.middleware_data.get('cache')
    bot: Bot = dialog_manager.middleware_data['bot']
    await cache.set_data(
        user_id=message.from_user.id,
        key=CacheKeys.UserData.age(),
        value=text
    )
    await dialog_manager.switch_to(state=ChangeDataSG.change_data_menu)
    await bot.delete_messages(chat_id=message.chat.id,
                              message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])


async def change_data_correct_weight_handler(message: Message,
                                             widget: ManagedTextInput,
                                             dialog_manager: DialogManager,
                                             text: str):
    cache: Cache = dialog_manager.middleware_data.get('cache')
    bot: Bot = dialog_manager.middleware_data['bot']
    await cache.set_data(
        user_id=message.from_user.id,
        key=CacheKeys.UserData.weight(),
        value=text
    )
    await dialog_manager.switch_to(state=ChangeDataSG.change_data_menu)
    await bot.delete_messages(chat_id=message.chat.id,
                              message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])


async def change_data_correct_height_handler(message: Message,
                                             widget: ManagedTextInput,
                                             dialog_manager: DialogManager,
                                             text: str):
    cache: Cache = dialog_manager.middleware_data.get('cache')
    bot: Bot = dialog_manager.middleware_data['bot']
    await cache.set_data(
        user_id=message.from_user.id,
        key=CacheKeys.UserData.height(),
        value=text
    )
    await dialog_manager.switch_to(state=ChangeDataSG.change_data_menu)
    await bot.delete_messages(chat_id=message.chat.id,
                              message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])


async def change_data_correct_calories_handler(message: Message,
                                               widget: ManagedTextInput,
                                               dialog_manager: DialogManager,
                                               text: str):
    cache: Cache = dialog_manager.middleware_data.get('cache')
    bot: Bot = dialog_manager.middleware_data['bot']
    await cache.set_data(
        user_id=message.from_user.id,
        mapping_values={CacheKeys.Calories.maximum_quantity(): text,
                        CacheKeys.Settings.automatic_calorie_counting(): RecountCalories.OFF}
    )

    await dialog_manager.switch_to(state=ChangeDataSG.change_data_menu)
    await bot.delete_messages(chat_id=message.chat.id,
                              message_ids=[message.message_id, message.message_id - 1, message.message_id - 2])


async def save_new_user_data_onclick(callback: CallbackQuery,
                                     widget: Button,
                                     dialog_manager: DialogManager):
    user_id = callback.from_user.id
    cache: Cache = dialog_manager.middleware_data.get('cache')
    session: AsyncSession = dialog_manager.middleware_data.get('session')
    user_data = await cache.get_all_data(user_id=dialog_manager.event.from_user.id)
    if user_data[CacheKeys.Settings.automatic_calorie_counting()] == RecountCalories.ON:
        calories = counting_calories(user_data=user_data)
        await cache.set_data(
            user_id=dialog_manager.event.from_user.id,
            key=CacheKeys.Calories.maximum_quantity(),
            value=calories if calories != 'None' else ''
        ) if calories is not None else ...

    await update_user_data(
        user_id=user_id,
        session=session,
        user_data={
            CacheKeys.UserData.gender(): user_data[CacheKeys.UserData.gender()],
            CacheKeys.UserData.activity(): user_data[CacheKeys.UserData.activity()],
            CacheKeys.UserData.age(): user_data[CacheKeys.UserData.age()],
            CacheKeys.UserData.weight(): user_data[CacheKeys.UserData.weight()],
            CacheKeys.UserData.height(): user_data[CacheKeys.UserData.height()],
            CacheKeys.Calories.maximum_quantity(): user_data[CacheKeys.Calories.maximum_quantity()],
            CacheKeys.Settings.automatic_calorie_counting(): bool(
                user_data[CacheKeys.Settings.automatic_calorie_counting()])
        }
    )


async def cancel_new_user_data_onclick(callback: CallbackQuery,
                                       widget: Button,
                                       dialog_manager: DialogManager):
    user_id = callback.from_user.id
    cache: Cache = dialog_manager.middleware_data.get('cache')
    session: AsyncSession = dialog_manager.middleware_data.get('session')
    user_data = await get_db_user_data(user_id=user_id, session=session)

    await cache.set_data(user_id=user_id, mapping_values=user_data)
