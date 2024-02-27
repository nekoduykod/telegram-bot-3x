# import asyncio
# from aiogram.types import Message
# from aiogram import Router

# from data.config import ADMINS
# from loader import db, bot
# import pandas as pd


# admin_router = Router()


# @admin_router.message(text="/allusers", user_id=ADMINS)
# async def get_all_users(message: Message):
#     users = await db.select_all_users()
#     id = []
#     name = []
#     for user in users:
#         id.append(user[-1])
#         name.append(user[1])
#     data = {
#         "Telegram ID": id,
#         "Name": name
#     }
#     pd.options.display.max_rows = 10000
#     df = pd.DataFrame(data)
#     if len(df) > 50:
#         for x in range(0, len(df), 50):
#             await bot.send_message(message.chat.id, df[x:x + 50])
#     else:
#        await bot.send_message(message.chat.id, df)
       

# @router_admin.message(text="/advertisment", user_id=ADMINS)
# async def send_ad_to_all(message: Message):
#     users = await db.select_all_users()
#     for user in users:
#         user_id = user[-1]
#         await bot.send_message(chat_id=user_id, text="TODO")
#         await asyncio.sleep(0.05)

# @router_admin.message(text="/cleandb", user_id=ADMINS)
# async def get_all_users(message: Message):
#     await db.delete_users()
#     await message.answer("TODO")