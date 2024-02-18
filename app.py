''' I`ve put everything to main file. I did not separate into loader+app.py '''
# # from utils.db_api.postgresql import Database
# from bot.data.config import BOT_TOKEN
# from bot.utils.set_bot_commands import set_default_commands
# from loader import dp, bot

# async def on_startup(dp):
#     from bot.utils.notify_admins import on_startup_notify

#     import bot.middlewares
#     bot.middlewares.setup(dp)
#     await set_default_commands(dp)
#     await on_startup_notify(dp)

# async def on_shutdown(dp):
#     from bot.utils.notify_admins import on_shutdown_notify
#     await on_shutdown_notify(dp)
#     await bot.close()

# if __name__ == '__main__':
#     from aiogram import executor
#     from bot.handlers.users import *

#     executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)