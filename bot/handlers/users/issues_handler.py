import re

from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import Router

from bot.keyboards.inline import keyboards_menu
from bot.handlers.users.photo_url_handler import LeavePhoto
from bot.states.states import ChooseButton, Issue1Form
from bot.data.text import item1_text, num_one_two_text, leave_photo_url_text


issue_router = Router()


@issue_router.message(Command(commands=["issues"]))
async def choose_issue(bot, message: Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Оберіть питання, що турбує.💭',
                           reply_markup=keyboards_menu.inline_kb)
    await ChooseButton.Issues.set()


@issue_router.callback_query(lambda query: re.match('^Issue[1-2]$', query.data), ChooseButton.Issues)
async def chosen_issue_callback(bot, call: CallbackQuery, state: FSMContext):
    if call.data == 'Issue1':
        location = call.data
        await state.update_data(location=location)
        await bot.send_message(chat_id=call.message.chat.id, text=item1_text, reply_markup=ReplyKeyboardRemove())
        await call.answer(text='Issue 1 chosen')
        await Issue1Form.Item1.set()

    # elif call.data == 'Issue2':
    #     location = call.data
    #     await state.update_data(location=location)
    #     await bot.send_message(chat_id=call.message.chat.id, text=item1_text, reply_markup=types.ReplyKeyboardRemove())
    #     await call.answer(text='Issue 2 chosen')
    #     await Issue2Form.Item1.set()

    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


# Issue 1 Question 1 
@issue_router.message(Issue1Form.Item1)
async def process_issue1_item1(bot, message: Message, state: FSMContext):
    if message.text == '1':
        await state.update_data(item1_response='Skip')
        await LeavePhoto.URL.set()
        await bot.send_message(message.chat.id, text=leave_photo_url_text)

    elif message.text == '2':
        await bot.send_message(message.chat.id, text="Коментар для уточнюючого питання:")
        await state.set_state(Issue1Form.Item2)
        await state.update_data(item1_response=None)
    else:
        await bot.send_message(message.chat.id, text=num_one_two_text)

@issue_router.message(Issue1Form.Item1_comment)
async def process_issue1_item1_comment(bot, message: Message, state: FSMContext):
    await state.update_data(item1_response=message.text)

    await bot.send_message(message.chat.id, text=leave_photo_url_text)
    await LeavePhoto.URL.set()