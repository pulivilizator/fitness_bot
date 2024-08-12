from typing import Optional
from bot.src.utils.enums import ActiveLevel, Sex
from bot.src.data_stores import CacheKeys


def get_active_multiplier(active: str) -> float:
    match active:
        case ActiveLevel.HIGH:
            return 1.5
        case ActiveLevel.MEDIUM:
            return 1.3
        case ActiveLevel.LOW:
            return 1.1
        case _:
            return 1


def counting_calories(user_data: dict, user_keys_id=False) -> Optional[int]:
    multiplier = get_active_multiplier(
        user_data.get(CacheKeys.UserData.activity(key_to_id=user_keys_id))
    )
    try:
        sex = user_data.get(CacheKeys.UserData.gender(key_to_id=user_keys_id))
        age = int(user_data.get(CacheKeys.UserData.age(key_to_id=user_keys_id)))
        height = int(user_data.get(CacheKeys.UserData.height(key_to_id=user_keys_id)))
        weight = int(user_data.get(CacheKeys.UserData.weight(key_to_id=user_keys_id)))
    except (TypeError, ValueError):
        return
    if sex == Sex.MALE:
        return int(((height * 5) - (age * 6.8) + (weight * 13.7) + 66) * multiplier)
    elif sex == Sex.FEMALE:
        return int(((height * 1.8) - (age * 4.7) + (weight * 9.6) + 665) * multiplier)
