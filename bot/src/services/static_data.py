import enum

TIMEZONE_URL = "https://api.geoapify.com/v1/geocode/search?text={text}&limit=1&apiKey={token}"


class UserStatus(enum.Enum):
    NEW = 'new'
    USER = 'user'
    ADMIN = 'admin'


class Language(enum.Enum):
    RU = 'ru'
    EN = 'en'


class ActiveLevel(enum.Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'


class Sex(enum.Enum):
    MALE = 'male'
    FEMALE = 'female'


class RecountCalories(enum.Enum):
    ON = 1
    OFF = 0
