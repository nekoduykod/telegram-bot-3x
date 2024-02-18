from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hbold

from main import bot, dp, types
from bot.data.text import welcome_text
# from bot.utils.misc import rate_limit


# @rate_limit(limit=5)  # Anti-spam
@dp.message_handler(Command('start'))
async def start_cmd(message: types.Message):
    reply_text = f'{hbold(message.from_user.first_name)}, {welcome_text}'
    await bot.send_message(chat_id=message.from_user.id, 
                           text=reply_text)


@dp.message_handler(commands=['exit'], state="*")
async def exit_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Exiting...🚀 Обери команду: /request_chatgpt, /issues, /help, /donate")