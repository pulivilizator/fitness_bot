from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Cancel, SwitchTo, Row, Radio, Column
from aiogram_dialog.widgets.text import Format

from bot.src.data_stores import CacheKeys
from bot.src.filters import age_check, weight_check, height_check, calories_check
from bot.src.handlers.user_parameter_handlers import incorrect_message_handler, incorrect_text_handler
from bot.src.states import ChangeDataSG
from bot.src.setters import SetButtonChecked

from .handlers import (change_data_sex_handler, change_data_correct_age_handler, change_data_activity_handler,
                       change_data_correct_height_handler, change_data_correct_weight_handler,
                       change_data_correct_calories_handler, update_calories_handler)
from .getters import (get_common_text, get_menu, get_sexes,
                      get_age, get_activities, get_height,
                      get_weight, get_calories)

change_data_dialog = Dialog(
    Window(
        Format('{change_data_menu_message}'),
        SwitchTo(text=Format('{change_data_sex_button}'),
                 state=ChangeDataSG.change_data_sex,
                 id='change_data_sex'),
        SwitchTo(text=Format('{change_data_age_button}'),
                 state=ChangeDataSG.change_data_age,
                 id='change_data_age'),
        SwitchTo(text=Format('{change_data_activity_button}'),
                 state=ChangeDataSG.change_data_activity,
                 id='change_data_activity'),
        SwitchTo(text=Format('{change_data_weight_button}'),
                 state=ChangeDataSG.change_data_weight,
                 id='change_data_weight'),
        SwitchTo(text=Format('{change_data_height_button}'),
                 state=ChangeDataSG.change_data_height,
                 id='change_data_height'),
        SwitchTo(text=Format('{change_data_calories_button}'),
                 state=ChangeDataSG.change_data_calories,
                 id='change_data_calories'),

        Cancel(Format('{change_data_save_update_calories}')),
        Cancel(Format('{previous_button}')),
        state=ChangeDataSG.change_data_menu,
        getter=get_menu
    ),

    Window(
        Format('{change_data_sex_message}'),
        Row(
            Radio(
                checked_text=Format('🔘 {item[1]}'),
                unchecked_text=Format('⚪️ {item[1]}'),
                id=CacheKeys.UserData.gender(key_to_id=True),
                item_id_getter=lambda x: x[0],
                items='sexes',
                on_state_changed=change_data_sex_handler
            ),
        ),
        SwitchTo(Format('{previous_button}'),
                 state=ChangeDataSG.change_data_menu,
                 id='back_to_menu'),
        state=ChangeDataSG.change_data_sex,
        getter=get_sexes
    ),
    Window(
        Format('{change_data_activity_message}'),
        Column(
            Radio(
                checked_text=Format('🔘 {item[1]}'),
                unchecked_text=Format('⚪️ {item[1]}'),
                id=CacheKeys.UserData.activity(key_to_id=True),
                item_id_getter=lambda x: x[0],
                items='activity_levels',
                on_state_changed=change_data_activity_handler
            )
        ),
        SwitchTo(Format('{previous_button}'),
                 state=ChangeDataSG.change_data_menu,
                 id='back_to_menu'),
        state=ChangeDataSG.change_data_activity,
        getter=get_activities
    ),
    Window(
        Format('{change_data_age_message}'),
        TextInput(
            id=CacheKeys.UserData.age(key_to_id=True),
            type_factory=age_check,
            on_success=change_data_correct_age_handler,
            on_error=incorrect_text_handler
        ),
        MessageInput(
            func=incorrect_message_handler,
            content_types=ContentType.ANY
        ),
        SwitchTo(Format('{previous_button}'),
                 state=ChangeDataSG.change_data_menu,
                 id='back_to_menu'),
        state=ChangeDataSG.change_data_age,
        getter=get_age
    ),
    Window(
        Format('{change_data_weight_message}'),
        TextInput(
            id=CacheKeys.UserData.weight(key_to_id=True),
            type_factory=weight_check,
            on_success=change_data_correct_weight_handler,
            on_error=incorrect_text_handler
        ),
        MessageInput(
            func=incorrect_message_handler,
            content_types=ContentType.ANY
        ),
        SwitchTo(Format('{previous_button}'),
                 state=ChangeDataSG.change_data_menu,
                 id='back_to_menu'),
        state=ChangeDataSG.change_data_weight,
        getter=get_weight
    ),
    Window(
        Format('{change_data_height_message}'),
        TextInput(
            id=CacheKeys.UserData.height(key_to_id=True),
            type_factory=height_check,
            on_success=change_data_correct_height_handler,
            on_error=incorrect_text_handler
        ),
        MessageInput(
            func=incorrect_message_handler,
            content_types=ContentType.ANY
        ),
        SwitchTo(Format('{previous_button}'),
                 state=ChangeDataSG.change_data_menu,
                 id='back_to_menu'),
        state=ChangeDataSG.change_data_height,
        getter=get_height
    ),
    Window(
        Format('{change_data_calories_message}'),
        TextInput(
            id=CacheKeys.Calories.maximum_quantity(key_to_id=True),
            type_factory=calories_check,
            on_success=change_data_correct_calories_handler,
            on_error=incorrect_text_handler
        ),
        MessageInput(
            func=incorrect_message_handler,
            content_types=ContentType.ANY
        ),
        SwitchTo(Format('{previous_button}'),
                 state=ChangeDataSG.change_data_menu,
                 id='back_to_menu'),
        state=ChangeDataSG.change_data_calories,
        getter=get_calories
    ),
    on_start=SetButtonChecked(
        CacheKeys.UserData.gender,
        CacheKeys.UserData.activity
    ),
    getter=get_common_text,
    on_close=update_calories_handler
)
