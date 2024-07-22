from typing import Any


def weight_check(text: Any, *args, **kwargs):
    if text.isdigit() and 15 <= int(text) <= 200:
        return text
    raise ValueError('weight')


def height_check(text: Any):
    if text.isdigit() and 50 <= int(text) <= 300:
        return text
    raise ValueError('height')


def age_check(text: Any):
    if text.isdigit() and 3 <= int(text) <= 150:
        return text
    raise ValueError('age')


def calories_check(text: Any):
    if text.isdigit():
        return text
    raise ValueError('calories')


def geo_check(text: Any):
    if (text[0] in ('+', '-') and  # начинается чи часовой пояс в плюса или минуса
            ':' in text and  # указаны ли минуты согласно паттерну
            text[1:].split(':')[0].isdigit() and  # правильный ли формат часов
            0 < int(text[1:].split(':')[0]) <= 24 and  # проверка диапазона часов
            text.split(':')[1].isdigit() and  # правильный ли формат минут
            0 <= int(text.split(':')[1]) < 60  # проверка диапазона минут
    ):
        return text
    elif 1 < len(text[1:].split(',')) < 4:
        return text
    raise ValueError('geo')
