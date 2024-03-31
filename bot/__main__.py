from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram_dialog import setup_dialogs

from redis.asyncio import Redis

import asyncio
import logging

from .config import get_config
from .src import set_menu, get_routers, Cache, CacheMiddleware, create_translator_hub, TranslatorRunnerMiddleware


async def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='[#{levelname} - {asctime}]\n{filename} - {name}|{funcName} - {lineno}: {message}\n',
                        style='{')

    config = get_config()

    r = Redis(host=config.redis.host, port=config.redis.port)
    user_cache = Cache(r)
    hub = create_translator_hub()
    session = AiohttpSession()

    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.workflow_data.update({'cache': user_cache,
                             'hub': hub,
                             'aiohttp_session': session,
                             'geoapify_token': config.geoapify.token})
    dp.include_routers(*get_routers())
    dp.startup.register(set_menu)
    dp.update.middleware(CacheMiddleware())
    dp.update.middleware(TranslatorRunnerMiddleware())
    setup_dialogs(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())