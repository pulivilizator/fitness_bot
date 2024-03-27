from aiogram.fsm.state import State, StatesGroup


class UserRegisterSG(StatesGroup):
    start = State()
    sex = State()
    active = State()
    weight = State()
    height = State()
    age = State()
    finish = State()


class MainMenuSG(StatesGroup):
    main_menu = State()


class SubtractCaloriesSG(StatesGroup):
    substract = State()


class PlusCaloriesSG(StatesGroup):
    plus = State()


class ChangeDataSG(StatesGroup):
    change_data_menu = State()
    change_data_sex = State()
    change_data_age = State()
    change_data_activity = State()
    change_data_weight = State()
    change_data_height = State()
    change_data_calories = State()


class SettingsSG(StatesGroup):
    settings_menu = State()
    change_language = State()
