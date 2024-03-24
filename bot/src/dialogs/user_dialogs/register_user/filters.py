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
