# from aiogram.types import Message
# from aiogram import Router


# echo_router = Router()

''' it simply returns your message back.'''
# @echo_router.message()
# async def echo_handler(message: Message):
#     """
#     Handler will forward receive a message back to the sender

#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("I did not understand")