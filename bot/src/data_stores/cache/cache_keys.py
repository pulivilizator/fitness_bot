from typing import Sequence


class KeysConverter:
    def __init__(self, *args: Sequence):
        self._keys: list = list(args)

    def __getattr__(self, item):
        return self.__class__(*(self._keys + [item]))

    def __str__(self, id=False):
        if not id:
            return ':'.join(self._keys)
        return '_'.join(self._keys)


class CacheKeys:
    @staticmethod
    def status(key_to_id=False) -> str:
        return KeysConverter('status').__str__(id=key_to_id)

    class UserData:
        @staticmethod
        def gender(key_to_id=False) -> str:
            return KeysConverter('user_data', 'gender').__str__(id=key_to_id)

        @staticmethod
        def activity(key_to_id=False) -> str:
            return KeysConverter('user_data', 'activity').__str__(id=key_to_id)

        @staticmethod
        def weight(key_to_id=False) -> str:
            return KeysConverter('user_data', 'weight').__str__(id=key_to_id)

        @staticmethod
        def height(key_to_id=False) -> str:
            return KeysConverter('user_data', 'height').__str__(id=key_to_id)

        @staticmethod
        def age(key_to_id=False) -> str:
            return KeysConverter('user_data', 'age').__str__(id=key_to_id)

    class Calories:
        @staticmethod
        def current_quantity(key_to_id=False) -> str:
            return KeysConverter('calories', 'current').__str__(id=key_to_id)

        @staticmethod
        def maximum_quantity(key_to_id=False) -> str:
            return KeysConverter('calories', 'maximum').__str__(id=key_to_id)

    class Settings:
        @staticmethod
        def language(key_to_id=False) -> str:
            return KeysConverter('settings', 'language').__str__(id=key_to_id)

        @staticmethod
        def automatic_calorie_counting(key_to_id=False):
            return KeysConverter('settings', 'automatic_calorie_counting').__str__(id=key_to_id)

        @staticmethod
        def timezone(key_to_id=False) -> str:
            return KeysConverter('settings', 'timezone').__str__(id=key_to_id)