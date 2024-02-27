import logging
 
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from bot.data.config import OPENAI_API_KEY
import openai


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


gpt_router = Router()


@gpt_router.message(Command(commands=["gpt_request"]))
async def gpt_request_cmd(message: Message):
    await message.delete()
    await message.answer(text="Please describe your question.")

@gpt_router.message(F.text & ~F.text.startswith('/'))
async def process_gpt_request(message: Message):
    request_text = message.text.strip()
    user_id = message.from_user.id
    try:
        prompt_text = "Analyze the following request: " + request_text

        response = openai.Completion.create(
            engine="text-davinci-002",  # TODO change better model. Turbo maybe
            prompt=prompt_text,
            max_tokens=1000
        )

        chatgpt_response = response.choices[0].text.strip()

        await message.bot.send_message(user_id, text=chatgpt_response)
        await message.bot.send_message(user_id, text="Thank you. Feel free to reach out.")

    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API Error: {e}")
        await message.bot.send_message(user_id, text="👾Oops. Sorry. We're working on it. Please try again later.")

    except Exception as e:
        logging.exception(f"Unexpected Error: {e}")
        await message.bot.send_message(user_id, text="Oops! Technical difficulties. Please try again later.")