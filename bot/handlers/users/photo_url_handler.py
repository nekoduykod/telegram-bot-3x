from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router

from bot.handlers.users.request_chatgpt import request_gpt_clarifying_issue
from bot.states.states import LeavePhoto
from bot.data.text import num_one_two_text, leave_photo_url_text


photoURL_router = Router()


@photoURL_router.message(LeavePhoto.URL)
async def leave_photo_url(bot, message: Message, state: FSMContext):
    if message.text == '1':
        await state.update_data(photo_url_reponse='Skip')
        await bot.send_message(message.chat.id, text="Усьо! Обробляємо🧠, стривайте.")
        await request_gpt_clarifying_issue(state)
    elif message.text == '2':
        await bot.send_message(message.chat.id, text=leave_photo_url_text)
        await state.set_state(LeavePhoto.URL_processing)
        await state.update_data(photo_url_reponse=None)
    else:
        await bot.send_message(message.chat.id, text=num_one_two_text)

@photoURL_router.message(LeavePhoto.URL_processing)
async def photo_url_processing(bot, message: Message, state: FSMContext):
    await state.update_data(photo_url_reponse=message.text)

    await bot.send_message(message.chat.id, text="🛠 Обробка запиту. Стривайте.")
    await request_gpt_clarifying_issue(state)