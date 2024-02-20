import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import DefaultBotProperties
from aiogram.enums import ParseMode

# from utils.db_api.postgresql import Database
from bot.data.config import BOT_TOKEN
from bot.utils.set_bot_commands import set_default_commands
from bot.handlers.users import user_routers


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    # db = Database()
    dp.include_router(user_routers)
    await set_default_commands(dp)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO)
    asyncio.run(main())


# old 2.25
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
    
    # executor.start_polling(dp, skip_updates=False, 
    #                        on_startup=on_startup, 
    #                        on_shutdown=on_shutdown, 
    #                        allowed_updates=["message", "callback_query"])