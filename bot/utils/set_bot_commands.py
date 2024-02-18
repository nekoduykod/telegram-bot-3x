from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", '/start'),
        types.BotCommand("help", 'instructions'),
        types.BotCommand("gpt_request", 'request ChatGPT directly'),
        types.BotCommand("issues", 'answer on clarifying questions before request'),
        types.BotCommand("exit", 'returns to main menu'),
        types.BotCommand("donate", '🌻links for 🇺🇦charities'),
        #TODO contac_centre / email us
    ])