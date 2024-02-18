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