from typing import Optional
from bot.src.utils import ActiveLevel, Sex, UserKeys


def get_active_multiplier(active: str) -> float:
    match active:
        case ActiveLevel.HIGH.value:
            return 1.5
        case ActiveLevel.MEDIUM.value:
            return 1.3
        case ActiveLevel.LOW.value:
            return 1.1
        case _:
            return 1


def counting_calories(user_data: dict, user_keys_id=False) -> Optional[int]:
    multiplier = get_active_multiplier(
        user_data.get(UserKeys.UserData.activity(key_to_id=user_keys_id))
    )
    try:
        sex = user_data.get(UserKeys.UserData.gender(key_to_id=user_keys_id))
        age = int(user_data.get(UserKeys.UserData.age(key_to_id=user_keys_id)))
        height = int(user_data.get(UserKeys.UserData.height(key_to_id=user_keys_id)))
        weight = int(user_data.get(UserKeys.UserData.weight(key_to_id=user_keys_id)))
    except TypeError:
        return
    if sex == Sex.MALE.value:
        return int(((height * 5) - (age * 6.8) + (weight * 13.7) + 66) * multiplier)
    elif sex == Sex.FEMALE.value:
        return int(((height * 1.8) - (age * 4.7) + (weight * 9.6) + 665) * multiplier)
