import logging
from typing import TypeAlias, Optional, Sequence

from redis.asyncio import Redis

class RedisKeys:
    def __init__(self, *args: Sequence):
        self._keys: list = list(args)

    def __getattr__(self, item):
        return self.__class__(*(self._keys + [item]))

    def __str__(self, id=False):
        if not id:
            return ':'.join(self._keys)
        return '_'.join(self._keys)


class UserKeys:
    settings = RedisKeys('change_data')
    status = RedisKeys('status')

    class Settings:
        language = RedisKeys('change_data', 'language')
        gender = RedisKeys('change_data', 'gender')
        activity = RedisKeys('change_data', 'activity')
        weight = RedisKeys('change_data', 'weight')
        height = RedisKeys('change_data', 'height')
        age = RedisKeys('change_data', 'age')

    class Calories:
        current_quantity = RedisKeys('calories', 'current')
        maximum_quantity = RedisKeys('calories', 'maximum')


KeyType: TypeAlias = Optional[str]
ValueType: TypeAlias = Optional[str | bool | int]
MappingValuesType: TypeAlias = Optional[dict[KeyType, ValueType]]

logger = logging.getLogger(__name__)


class UserCache:
    def __init__(self, r: Redis):
        self._r = r

    async def set_data(self, user_id: int,
                       key: KeyType = None,
                       value: ValueType = None,
                       mapping_values: MappingValuesType = None) -> None:

        user_key = f'user:{user_id}'
        logger.info(f'{user_key} set data')
        if mapping_values:
            set_data = {k: str(v)
            if not isinstance(v, bool)
            else '0'
            if not v
            else '1'
                        for k, v in mapping_values.items()}
            await self._r.hset(name=user_key, mapping=set_data)
            return
        if isinstance(value, bool):
            value = int(value)
        await self._r.hset(name=user_key, key=str(key), value=str(value))

    async def get_value(self, user_id: int, key: KeyType = None) -> ValueType:
        user_key = f'user:{user_id}'

        user_bytes_value: Optional[bytes] = await self._r.hget(name=user_key, key=key)
        logger.info(f'{user_key} get value')

        if not user_bytes_value:
            return
        user_value = user_bytes_value.decode('utf-8-sig')

        return int(user_value) if user_value.isdigit() else user_value

    async def get_all_data(self, user_id: int) -> MappingValuesType:
        user_key = f'user:{user_id}'

        user_bytes_data: Optional[dict[bytes, bytes]] = await self._r.hgetall(name=user_key)
        logger.info(f'{user_key} get all values')

        if not user_bytes_data:
            return

        mapping_values = {key.decode('utf-8-sig'): int(value.decode('utf-8-sig'))
        if value.isdigit() else value.decode('utf-8-sig')
                          for key, value in user_bytes_data.items()}

        return mapping_values

    async def user_exists(self, user_id: int) -> bool:
        user_key = f'user:{user_id}'
        return await self._r.exists(user_key)

