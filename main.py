import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
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