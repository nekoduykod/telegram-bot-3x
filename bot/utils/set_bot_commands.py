from aiogram.types import BotCommand


async def set_default_commands(dp) -> None:
    commands = [
        BotCommand(command="start", description="Start the bot and access the main menu."),
        BotCommand(command="help", description="Get instructions on how to use the bot."),
        BotCommand(command="gpt_request", description="Request text generation from ChatGPT directly."),
        BotCommand(command="issues", description="Receive clarification and guidance before making a request."),
        BotCommand(command="exit", description="Return to the main menu."),
        BotCommand(command="donate", description="Find links to donate to Ukrainian charities."),
        # TODO: Add descriptions for "contact_centre" and "email_us" commands when implemented.
    ]
    try:
        await dp.bot.set_my_commands(commands)
    except Exception as e:
        # logging.error(f"Failed to set default bot commands: {e}")
        pass