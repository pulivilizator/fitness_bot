from aiogram_dialog import DialogManager

from bot.src.utils import UserKeys, UserStatus


def create_final_user_data(result_data: dict, dialog_manager: DialogManager) -> dict:
    return {
        UserKeys.UserData.language(): result_data.get(UserKeys.UserData.language(key_to_id=True)) or '',
        UserKeys.UserData.activity(): result_data.get(UserKeys.UserData.activity(key_to_id=True)) or '',
        UserKeys.UserData.gender(): result_data.get(UserKeys.UserData.gender(key_to_id=True)) or '',
        UserKeys.UserData.age(): result_data.get(UserKeys.UserData.age(key_to_id=True)) or '',
        UserKeys.UserData.weight(): result_data.get(UserKeys.UserData.weight(key_to_id=True)) or '',
        UserKeys.UserData.height(): result_data.get(UserKeys.UserData.height(key_to_id=True)) or '',
        UserKeys.Calories.maximum_quantity(): dialog_manager.dialog_data.get('max_calories'),
        UserKeys.Calories.current_quantity(): dialog_manager.dialog_data.get('current_calories'),
        UserKeys.status(): UserStatus.USER.value,
    }
