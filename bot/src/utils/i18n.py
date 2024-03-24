from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub() -> TranslatorHub:
    hub: TranslatorHub = TranslatorHub(
        locales_map={
            'ru': ('ru', 'en'),
            'en': ('en', 'ru')
        },
        translators=[
            FluentTranslator(
                locale='ru',
                translator=FluentBundle.from_files(
                    locale='ru-RU',
                    filenames=['bot/locales/ru/LC_MESSAGES/txt.ftl']
                )
            ),
            FluentTranslator(
                locale='en',
                translator=FluentBundle.from_files(
                    locale='en-US',
                    filenames=['bot/locales/en/LC_MESSAGES/txt.ftl']
                )
            )
        ]
    )
    return hub
