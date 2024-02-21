from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


help_router = Router()


@help_router.message(Command(commands=["help"]))
async def help(message: Message):
    await message.delete()
    await message.answer(" - Ask our AI 🤖\n"
                         " - Exit🧹 - returns to main menu\n")