from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class AioRedis:
    host: str
    port: int


@dataclass
class Geoapify:
    token: str


@dataclass
class Config:
    tg_bot: TgBot
    redis: AioRedis
    geoapify: Geoapify


def get_config():
    env = Env()
    env.read_env()

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
        ),
        redis=AioRedis(
            host=env('REDIS_HOST'),
            port=env('REDIS_PORT')
        ),
        geoapify=Geoapify(
            token=env('GEOAPIFY_TOKEN')
        )
    )
