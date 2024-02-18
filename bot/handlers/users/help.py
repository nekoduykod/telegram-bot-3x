from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from main import dp
from bot.utils.misc import rate_limit


@rate_limit(limit=5)  # Anti-spam
@dp.message_handler(Command("help"))
async def start(message: Message):
    await message.answer(" - You can ask ChatGPT directly 🤖\n"
                         " - Choose issue and answer questions💬\n"
                         " You can skip or answer✅\n"
                         " - Exit🧹 - returns to main menu\n"
                         " - Donate💙💛 - popular charity links\n")