from datetime import datetime

from sqlalchemy import BigInteger, DateTime, func, Enum as SQLAlchemyEnum, SmallInteger, ForeignKey, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.src.data_stores.db.base import Base
from bot.src.utils.enums import ActiveLevel, Sex, UserStatus, Language


class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    activity_level: Mapped[str] = mapped_column(SQLAlchemyEnum(ActiveLevel), nullable=True)
    gender: Mapped[str] = mapped_column(SQLAlchemyEnum(Sex), nullable=True)
    weight: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    height: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    age: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    status: Mapped[str] = mapped_column(SQLAlchemyEnum(UserStatus), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 nullable=False,
                                                 server_default=func.now())
    last_updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, onupdate=func.now())
    settings: Mapped['UserSettings'] = relationship(back_populates='user', uselist=False)


class UserSettings(Base):
    __tablename__ = 'user_settings'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    language: Mapped[str] = mapped_column(SQLAlchemyEnum(Language), nullable=False, default=Language.EN)
    automatic_calorie_counting: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    timezone: Mapped[str] = mapped_column(String(7), nullable=False)
    last_updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, onupdate=func.now())

    user_id: Mapped[int] = mapped_column(BigInteger,
                                         ForeignKey('users.telegram_id'),
                                         nullable=False)

    user: Mapped['User'] = relationship(back_populates='settings')
