import enum
from enum import StrEnum, IntEnum
TIMEZONE_URL = "https://api.geoapify.com/v1/geocode/search?text={text}&limit=1&apiKey={token}"


class UserStatus(StrEnum):
    NEW = 'new'
    USER = 'user'
    ADMIN = 'admin'


class Language(StrEnum):
    RU = 'ru'
    EN = 'en'


class ActiveLevel(StrEnum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class Sex(StrEnum):
    MALE = 'male'
    FEMALE = 'female'


class RecountCalories(IntEnum):
    ON = 1
    OFF = 0
