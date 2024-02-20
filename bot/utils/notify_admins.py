import logging

from aiogram import Dispatcher

from bot.data.config import ADMINS_ID


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS_ID:
        try:
            await dp.bot.send_message(admin, "***Це повідомлення бачать тільки адміни***\n"
                                             "БОТ ЗАПУЩЕНИЙ")
        except Exception as err:
            logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    for admin in ADMINS_ID:
        try:
            await dp.bot.send_message(admin, "***Це повідомлення бачать тільки адміни***\n"
                                             "БОТ ВИМКНЕНИЙ")
        except Exception as err:
            logging.exception(err)


# import logging
# from aiogram import Bot

# from core.config import ADMINS


# async def on_startup_notify(bot: Bot):
#     """Notify admins about successful start"""
#     for admin in ADMINS:
#         try:
#             await bot.send_message(chat_id=admin, text="Bot ishga tushdi.")
#         except Exception as err:
#             logging.exception(err)


# async def on_shutdown_notify(bot: Bot):
#     """Notify admins about successful stop"""
#     for admin in ADMINS:
#         try:
#             await bot.send_message(chat_id=admin, text="Bot to'xtadi.")
#         except Exception as err:
#             logging.exception(err)