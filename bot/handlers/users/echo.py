from aiogram import types

from main import dp


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo_message(message: types.Message):
    """Answer for photo messages"""
    await message.answer("I work with text only 📝")