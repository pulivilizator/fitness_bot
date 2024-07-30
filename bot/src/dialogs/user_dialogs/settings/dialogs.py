from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Back, SwitchTo, Row, Radio, Cancel, Checkbox
from aiogram_dialog.widgets.text import Format

from bot.src.states import SettingsSG
from bot.src.data_stores import CacheKeys
from .getters import get_langs, settings_menu_getter, get_common_text
from .handlers import settings_calories_counting_handler, to_menu_onclick

from ..register_user.handlers import change_lang_handler
from bot.src.setters import SetButtonChecked

settings_dialog = Dialog(
    Window(
        Format('{settings_message}'),

        Checkbox(
            checked_text=Format('{calories_counting_on}'),
            unchecked_text=Format('{calories_counting_off}'),
            id=CacheKeys.Settings.automatic_calorie_counting(key_to_id=True),
            on_state_changed=settings_calories_counting_handler
        ),

        SwitchTo(text=Format('{change_language_button}'),
                 state=SettingsSG.change_language,
                 id='change_language'),

        Cancel(Format('{previous_button}'), id='previous', on_click=to_menu_onclick),
        state=SettingsSG.settings_menu,
        getter=settings_menu_getter
    ),
    Window(
        Format('{change_language_message}'),
        Row(
            Radio(
                checked_text=Format('🔘 {item[1]}'),
                unchecked_text=Format('⚪️ {item[1]}'),
                id=CacheKeys.Settings.language(key_to_id=True),
                item_id_getter=lambda x: x[0],
                on_state_changed=change_lang_handler,
                items='languages',
            ),
        ),
        SwitchTo(Format('{previous_button}'),
                 id='previous',
                 state=SettingsSG.settings_menu),
        getter=get_langs,
        state=SettingsSG.change_language,
    ),
    on_start=SetButtonChecked(CacheKeys.Settings.language,
                              CacheKeys.Settings.automatic_calorie_counting),
    getter=get_common_text
)
