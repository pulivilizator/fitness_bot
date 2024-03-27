from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Back, SwitchTo, Row, Radio, Cancel
from aiogram_dialog.widgets.text import Format

from bot.src.states import SettingsSG
from bot.src.services import UserCacheKeys
from .getters import get_langs, settings_menu_getter, get_common_text

from ..register_user.handlers import change_lang_handler, set_user_language


settings_dialog = Dialog(
    Window(
        Format('{settings_message}'),
        SwitchTo(text=Format('{change_language_button}'),
                 state=SettingsSG.change_language,
                 id='change_language'),

        Cancel(Format('{previous_button}'), id='previous'),
        state=SettingsSG.settings_menu,
        getter=settings_menu_getter
    ),
    Window(
        Format('{change_language_message}'),
        Row(
            Radio(
                checked_text=Format('🔘 {item[1]}'),
                unchecked_text=Format('⚪️ {item[1]}'),
                id=UserCacheKeys.Settings.language(key_to_id=True),
                item_id_getter=lambda x: x[0],
                on_state_changed=change_lang_handler,
                items='languages',
            ),
        ),
        Back(Format('{previous_button}'), id='previous'),
        getter=get_langs,
        state=SettingsSG.change_language,
    ),
    on_start=set_user_language,
    getter=get_common_text
)
