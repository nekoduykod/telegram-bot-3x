from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from aiogram.utils.markdown import hbold
from bot.data.text import welcome_text


on = Router()


@on.message(Command(commands=["start"]))
async def start_cmd(msg: Message) -> None:
    await msg.delete()
    await msg.answer(text=f'{hbold(msg.from_user.first_name)}, {welcome_text}')


''' it is when cancelling State. Useless for now '''
@on.message(Command(commands=["exit"]))
async def exit_handler(msg: Message, state: FSMContext) -> None:
    await msg.delete()
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await msg.answer("Exiting...🚀 Обери команду: /request_chatgpt, /issues, /help")