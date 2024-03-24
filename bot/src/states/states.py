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
    start_change_data = State()
