from aiogram import Bot
from aiogram.types import BotCommand

async def set_menu(bot: Bot):
    menu = [
        BotCommand(command='/start', description='show main menu message'),
        BotCommand(command='/help', description='show help message')
    ]

    await bot.set_my_commands(menu)
