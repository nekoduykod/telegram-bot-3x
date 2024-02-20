from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# from bot.utils.misc import rate_limit   . Obsolete. Actually, check middleware.throttling (rate_limit)


help_router = Router()


# @rate_limit(limit=5)  # Anti-spam
@help_router.message(Command(commands=["help"]))
async def help(message: Message):
    await message.delete()
    await message.answer(" - Ask AI directly 🤖\n"
                         " - Choose issue to answer clarifying questions before request💬\n"
                         " You can skip or answer✅\n"
                         " - Exit🧹 - returns to main menu\n"
                         " - Donate💙💛 - popular charity links\n")