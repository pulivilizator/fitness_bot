from aiogram.client.session.aiohttp import AiohttpSession
from aiogram_dialog import DialogManager

from .static_data import TIMEZONE_URL
from bot.src.db import CacheKeys


async def get_timezone_api(text: str, session: AiohttpSession, token: str) -> str:
    client = await session.create_session()
    async with client.get(url=TIMEZONE_URL.format(text=text, token=token),
                          headers={"Accept": "application/json"}) as response:
        json_resp = await response.json()
        return await json_validate(json_resp)


async def json_validate(json_resp: dict) -> str:
    if json_resp.get('features'):
        return json_resp['features'][0]['properties']['timezone']['offset_STD']
    raise ValueError('Invalid geo')


async def update_dialog_data(dialog_manager: DialogManager, text: str):
    if text[0] in ('+', '-'):
        dialog_manager.dialog_data.update({CacheKeys.Settings.timezone(key_to_id=True): text})
        return
    await get_timezone(dialog_manager, text)


async def get_timezone(dialog_manager: DialogManager, text: str):
    session = dialog_manager.middleware_data.get('aiohttp_session')
    geo_token = dialog_manager.middleware_data.get('geoapify_token')
    timezone = await get_timezone_api(text, session, geo_token)
    dialog_manager.dialog_data.update({CacheKeys.Settings.timezone(key_to_id=True): timezone})
