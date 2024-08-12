from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram_dialog import setup_dialogs
from nats.aio.client import Client as NATSClient
from nats.js import JetStreamContext

from redis.asyncio import Redis

import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker

from .config import get_config, Config
from .src import get_routers
from .storage import NatsStorage
from .src.utils import connect_to_nats, create_translator_hub
from .src.middlewares import TranslatorRunnerMiddleware, CacheMiddleware, DbSessionMiddleware
from .src.menu import set_menu
from .src.data_stores.cache import Cache

logging.basicConfig(level=logging.DEBUG,
                    format='[#{levelname} - {asctime}]\n{filename} - {name}|{funcName} - {lineno}: {message}\n',
                    style='{')


async def main():
    config = get_config()

    nc, js = await connect_to_nats(config.nats.servers)

    dp = await create_dispatcher(config,
                                 nc=nc,
                                 js=js)

    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    setup_dialogs(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def create_dispatcher(config: Config,
                            nc: NATSClient,
                            js: JetStreamContext) -> Dispatcher:
    storage = await NatsStorage(nc=nc, js=js).create_storage()
    dp = Dispatcher(storage=storage)

    engine = create_async_engine(
        url=config.db.dsn
    )
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False, autoflush=True)

    r = Redis(host=config.redis.host, port=config.redis.port)
    user_cache = Cache(r)

    hub = create_translator_hub()

    session = AiohttpSession()

    dp.workflow_data.update({'cache': user_cache,
                             'hub': hub,
                             'aiohttp_session': session,
                             'geoapify_token': config.geoapify.token})

    dp.include_routers(*get_routers())
    dp.startup.register(set_menu)
    dp.update.outer_middleware(DbSessionMiddleware(sessionmaker))
    dp.update.middleware(CacheMiddleware())
    dp.update.middleware(TranslatorRunnerMiddleware())

    return dp


if __name__ == '__main__':
    asyncio.run(main())
