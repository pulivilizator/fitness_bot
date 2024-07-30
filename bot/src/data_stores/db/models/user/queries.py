from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from .user import User, UserSettings, UserCalories
from bot.src.data_stores.cache.cache_keys import CacheKeys


async def create_user(tg_id: int, session: AsyncSession, user_data: dict):
    user = User(
        telegram_id=tg_id,
        status=user_data[CacheKeys.status()],
        activity=user_data[CacheKeys.UserData.activity()],
        gender=user_data[CacheKeys.UserData.gender()],
        weight=user_data[CacheKeys.UserData.weight()],
        height=user_data[CacheKeys.UserData.height()],
        age=user_data[CacheKeys.UserData.age()],
    )
    user_settings = UserSettings(
        timezone=user_data[CacheKeys.Settings.timezone()],
        language=user_data[CacheKeys.Settings.language()],
        user_id=user.telegram_id
    )
    user_calories = UserCalories(
        maximum=user_data[CacheKeys.Calories.maximum_quantity()],
        user_id=user.telegram_id
    )
    session.add_all([user, user_calories, user_settings])
    await session.commit()


async def get_user_data(session: AsyncSession, user_id: int) -> dict:
    stmt = select(User).where(user_id == User.telegram_id).options(joinedload(User.settings),
                                                                   joinedload(User.calories))
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    return {
        CacheKeys.status(): user.status,
        CacheKeys.UserData.activity(): user.activity,
        CacheKeys.UserData.gender(): user.gender,
        CacheKeys.UserData.weight(): user.weight,
        CacheKeys.UserData.height(): user.height,
        CacheKeys.UserData.age(): user.age,
        CacheKeys.Settings.timezone(): user.settings.timezone,
        CacheKeys.Settings.language(): user.settings.language,
        CacheKeys.Settings.automatic_calorie_counting(): user.settings.automatic_calorie_counting,
        CacheKeys.Calories.maximum_quantity(): user.calories.maximum,
        CacheKeys.Calories.current_quantity(): user.calories.current
    }


async def update_user_data(session: AsyncSession, user_id: int, user_data: dict):
    stmt = select(User).where(user_id == User.telegram_id).options(joinedload(User.calories), joinedload(User.settings))
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    for key, value in user_data.items():
        if key.startswith('user:'):
            user_key = key.split(':', 1)[1]
            if hasattr(user, user_key):
                setattr(user, key, value)
        elif key.startswith('calories:'):
            calories_key = key.split(':', 1)[1]
            if hasattr(user.calories, calories_key):
                setattr(user.calories, calories_key, value)
        elif key.startswith('settings:'):
            settings_key = key.split(':', 1)[1]
            if hasattr(user.settings, settings_key):
                setattr(user.settings, settings_key, value)

    await session.commit()
