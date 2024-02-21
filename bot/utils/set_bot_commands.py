import logging

from aiogram import Bot
from aiogram.types import BotCommand


async def set_default_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="Start the bot and access the main menu."),
        BotCommand(command="help", description="Get instructions on how to use the bot."),
        BotCommand(command="gpt_request", description="Request text generation from ChatGPT directly."),
        BotCommand(command="exit", description="Return to the main menu.")
    ]
    try:
        await bot.set_my_commands(commands)
    except Exception as e:
        logging.error(f"Failed to set default bot commands: {e}")
        pass