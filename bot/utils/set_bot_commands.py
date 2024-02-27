import logging

from aiogram import Bot
from aiogram.types import BotCommand


async def set_default_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="/start."),
        BotCommand(command="help", description="instructions"),
        BotCommand(command="gpt_request", description="request ChatGPT directly."),
        BotCommand(command="exit", description="exits a state")
    ]
    try:
        await bot.set_my_commands(commands)
    except Exception as e:
        logging.error(f"Failed to set default bot commands: {e}")
        pass