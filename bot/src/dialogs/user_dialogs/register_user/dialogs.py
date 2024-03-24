from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Next, Button, Radio, Column, Row, Back
from aiogram_dialog.widgets.text import Format

from bot.src.utils import UserKeys
from bot.src.states import UserRegisterSG

from .getters import (get_sexes, get_lang_and_hello, get_active_levels, get_age, get_height, get_weight,
                      get_register_finish)
from .filters import weight_check, height_check, age_check
from .handlers import (correct_parameters_handler, error_parameters_handler, change_lang_handler,
                       register_finish_handler)

register_dialog = Dialog(
    Window(
        Format('{hello_message}'),
        Next(Format(text='{hello_register}'), id='start_register'),
        Row(
            Radio(
                checked_text=Format('🔘 {item[1]}'),
                unchecked_text=Format('⚪️ {item[1]}'),
                id=UserKeys.Settings.language.__str__(id=True),
                item_id_getter=lambda x: x[0],
                on_state_changed=change_lang_handler,
                on_click=change_lang_handler,
                items='languages'
            ),
        ),
        state=UserRegisterSG.start,
        getter=get_lang_and_hello
    ),
    Window(
        Format('{sex_message}'),
        Row(
            Radio(
                checked_text=Format('🔘 {item[1]}'),
                unchecked_text=Format('⚪️ {item[1]}'),
                id=UserKeys.Settings.gender.__str__(id=True),
                item_id_getter=lambda x: x[0],
                items='sexes',
            ),
        ),
        Next(Format('{next}'), id='next_register'),
        Back(Format('{previous}'), id='back_register'),
        getter=get_sexes,
        state=UserRegisterSG.sex
    ),
    Window(
        Format('{activity_message}'),
        Column(
            Radio(
                checked_text=Format('🔘 {item[1]}'),
                unchecked_text=Format('⚪️ {item[1]}'),
                id=UserKeys.Settings.activity.__str__(id=True),
                item_id_getter=lambda x: x[0],
                items='active_levels',
            ),
        ),
        Next(Format('{next}'), id='next_register'),
        Back(Format('{previous}'), id='back_register'),
        getter=get_active_levels,
        state=UserRegisterSG.active
    ),
    Window(
        Format('{weight_message}'),
        TextInput(
            id=UserKeys.Settings.weight.__str__(id=True),
            type_factory=weight_check,
            on_success=correct_parameters_handler,
            on_error=error_parameters_handler
        ),
        MessageInput(
            func=error_parameters_handler,
            content_types=ContentType.ANY
        ),
        Next(Format('{next}'), id='next_register'),
        Back(Format('{previous}'), id='back_register'),
        state=UserRegisterSG.weight,
        getter=get_weight
    ),
    Window(
        Format('{height_message}'),
        TextInput(
            id=UserKeys.Settings.height.__str__(id=True),
            type_factory=height_check,
            on_success=correct_parameters_handler,
            on_error=error_parameters_handler
        ),
        MessageInput(
            func=error_parameters_handler,
            content_types=ContentType.ANY
        ),
        Next(Format('{next}'), id='next_register'),
        Back(Format('{previous}'), id='back_register'),
        state=UserRegisterSG.height,
        getter=get_height
    ),
    Window(
        Format('{age_message}'),
        TextInput(
            id=UserKeys.Settings.age.__str__(id=True),
            type_factory=age_check,
            on_success=correct_parameters_handler,
            on_error=error_parameters_handler
        ),
        MessageInput(
            func=error_parameters_handler,
            content_types=ContentType.ANY
        ),
        Next(Format('{next}'), id='next_register'),
        Back(Format('{previous}'), id='back_register'),
        state=UserRegisterSG.age,
        getter=get_age
    ),
    Window(
        Format('{register_finish_message}'),
        Button(
            text=Format('{register_finish_button}'),
            id='register_finish',
            on_click=register_finish_handler
        ),
        Back(Format('{previous}'), id='back_register'),
        getter=get_register_finish,
        state=UserRegisterSG.finish
    ),
)
