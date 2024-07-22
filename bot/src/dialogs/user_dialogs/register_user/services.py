from aiogram_dialog import DialogManager

from bot.src.utils.enums import UserStatus
from bot.src.data_stores import CacheKeys


def create_final_user_data(result_data: dict, dialog_manager: DialogManager) -> dict:
    return {
        CacheKeys.Settings.language(): result_data.get(CacheKeys.Settings.language(key_to_id=True)) or '',
        CacheKeys.UserData.activity(): result_data.get(CacheKeys.UserData.activity(key_to_id=True)) or '',
        CacheKeys.UserData.gender(): result_data.get(CacheKeys.UserData.gender(key_to_id=True)) or '',
        CacheKeys.UserData.age(): result_data.get(CacheKeys.UserData.age(key_to_id=True)) or '',
        CacheKeys.UserData.weight(): result_data.get(CacheKeys.UserData.weight(key_to_id=True)) or '',
        CacheKeys.UserData.height(): result_data.get(CacheKeys.UserData.height(key_to_id=True)) or '',
        CacheKeys.Calories.maximum_quantity(): dialog_manager.dialog_data.get('max_calories'),
        CacheKeys.Calories.current_quantity(): dialog_manager.dialog_data.get('current_calories'),
        CacheKeys.Settings.timezone(): dialog_manager.dialog_data.get(CacheKeys.Settings.timezone(key_to_id=True)) or '00:00',
        CacheKeys.status(): UserStatus.USER.value,
    }
