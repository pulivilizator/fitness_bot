from aiogram_dialog import DialogManager

from bot.src.services import UserCacheKeys, UserStatus


def create_final_user_data(result_data: dict, dialog_manager: DialogManager) -> dict:
    return {
        UserCacheKeys.Settings.language(): result_data.get(UserCacheKeys.Settings.language(key_to_id=True)) or '',
        UserCacheKeys.UserData.activity(): result_data.get(UserCacheKeys.UserData.activity(key_to_id=True)) or '',
        UserCacheKeys.UserData.gender(): result_data.get(UserCacheKeys.UserData.gender(key_to_id=True)) or '',
        UserCacheKeys.UserData.age(): result_data.get(UserCacheKeys.UserData.age(key_to_id=True)) or '',
        UserCacheKeys.UserData.weight(): result_data.get(UserCacheKeys.UserData.weight(key_to_id=True)) or '',
        UserCacheKeys.UserData.height(): result_data.get(UserCacheKeys.UserData.height(key_to_id=True)) or '',
        UserCacheKeys.Calories.maximum_quantity(): dialog_manager.dialog_data.get('max_calories'),
        UserCacheKeys.Calories.current_quantity(): dialog_manager.dialog_data.get('current_calories'),
        UserCacheKeys.status(): UserStatus.USER.value,
    }
