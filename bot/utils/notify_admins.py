# import logging

# from aiogram import Dispatcher
# from aiogram import Bot

# from bot.data.config import ADMINS_ID

# ''' code is shit. Needs to be refactored to fit aiogram 3+. 
# i dont like dp.bot.send_message and (bot: Bot, dp: Dispatcher). smells wrong '''

# async def on_startup_notify(bot: Bot, dp: Dispatcher):
#     for admin in ADMINS_ID:
#         try:
#             await dp.bot.send_message(admin, "***Це повідомлення бачать тільки адміни***\n"
#                                              "БОТ ЗАПУЩЕНИЙ")
#         except Exception as err:
#             logging.exception(err)


# async def on_shutdown_notify(bot: Bot, dp: Dispatcher):
#     for admin in ADMINS_ID:
#         try:
#             await dp.bot.send_message(admin, "***Це повідомлення бачать тільки адміни***\n"
#                                              "БОТ ВИМКНЕНИЙ")
#         except Exception as err:
#             logging.exception(err)