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
    if (text[0] in ('+', '-') and ':' in text and text[1:].split(':')[0].isdigit()) or 1 < len(text[1:].split(',')) < 4:
        return text
    raise ValueError('geo')
