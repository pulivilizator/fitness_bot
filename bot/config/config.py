from environs import Env
from dataclasses import dataclass

from .models import *


@dataclass
class Config:
    tg_bot: TgBot
    redis: AioRedis
    geoapify: Geoapify
    nats: Nats
    db: DbConfig


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
        ),
        nats=Nats(
            servers=[f'nats://{x}' for x in env.list('NATS_SERVERS', delimiter=' ')]
        ),
        db=DbConfig(
            dsn=env('DB_DSN')
        )
    )
