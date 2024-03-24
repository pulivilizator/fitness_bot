import enum


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
