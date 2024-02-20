from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from bot.data.text import welcome_text
# from bot.utils.misc import rate_limit # OBSOLETE. check middleware.throttling


start_router = Router()
exit_router = Router()


# @rate_limit(limit=5)  # Anti-spam
@start_router.message(Command(commands=["start"]))
async def start_cmd(message: Message) -> None:
    reply_text = f'{hbold(message.from_user.first_name)}, {welcome_text}'
    await message.answer(text=reply_text)


@exit_router.message(Command(commands=["exit"]))
async def exit_handler(message: Message, state: FSMContext) -> None:  # do i need FSM context here?
    await message.delete()
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer("Exiting...🚀 Обери команду: /request_chatgpt, /issues, /help, /donate")