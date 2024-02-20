from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.data.text import links_charities_text
# from bot.utils.misc import rate_limit   . Obsolete. Actually, check middleware.throttling (rate_limit)


donate_router = Router()


# @rate_limit(limit=3)  # Anti-spam
@donate_router.message(Command(commands=['donate']))
async def donate_links(bot, message: Message):
    await message.delete()
    await bot.send_message(chat_id=message.from_user.id, 
                           text=links_charities_text,
                           parse_mode="Markdown",
                           disable_web_page_preview=True)


# Can like this?
#     await message.answer(" - Ask AI directly 🤖\n"
#                          " - Choose issue to answer clarifying questions before request💬\n"
#                          " You can skip or answer✅\n"
#                          " - Exit🧹 - returns to main menu\n"
#                          " - Donate💙💛 - popular charity links\n")