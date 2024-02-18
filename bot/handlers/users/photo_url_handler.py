from aiogram import types
from main import bot, dp
from aiogram.dispatcher import FSMContext

from bot.handlers.users.request_chatgpt import process_checklist_answers_for_request
from bot.states.states import LeavePhoto
from bot.data.text import num_one_two_text, leave_photo_url_text


@dp.message_handler(state=LeavePhoto.URL)
async def leave_photo_url(message: types.Message, state: FSMContext):
    if message.text == '1':
        await state.update_data(photo_url_reponse='Skip')
        await bot.send_message(message.chat.id, text="Усьо! Обробляємо🧠, стривайте.")
        await process_checklist_answers_for_request(state)
    elif message.text == '2':
        await bot.send_message(message.chat.id, text=leave_photo_url_text)
        await state.set_state(LeavePhoto.URL_processing)
        await state.update_data(photo_url_reponse=None)
    else:
        await bot.send_message(message.chat.id, text=num_one_two_text)

@dp.message_handler(state=LeavePhoto.URL_processing)
async def photo_url_processing(message: types.Message, state: FSMContext):
    await state.update_data(photo_url_reponse=message.text)

    await bot.send_message(message.chat.id, text="🛠 Обробка запиту. Стривайте.")
    await process_checklist_answers_for_request(state)