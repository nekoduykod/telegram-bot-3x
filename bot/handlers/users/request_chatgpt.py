import logging
import json

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.data.config import OPENAI_API_KEY
import openai


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


gpt_router = Router()


@gpt_router.message(Command(commands=["gpt_request"]))
async def gpt_request_command(message: Message):
    await message.answer("Please describe your question.")


@gpt_router.message(lambda message: message.text and not message.text.startswith('/'))
async def process_gpt_request(message: Message):
    request_text = message.text.strip()
    await send_direct_gpt_request(request_text, message.from_user.id)

async def send_direct_gpt_request(bot, request_text: str, user_id: int):
    try:
        prompt_text = "Analyze the following request: " + request_text

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt_text,
            max_tokens=1000
        )

        chatgpt_response = response.choices[0].text.strip()

        await bot.send_message(user_id, text=chatgpt_response)
        await bot.send_message(user_id, text="Thank you. Feel free to reach out.")

    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API Error: {e}")
        await bot.send_message(user_id, text="👾Oops. Sorry. We're working on it. Please try again later.")

    except Exception as e:
        logging.exception(f"Unexpected Error: {e}")
        await bot.send_message(user_id, text="Oops! Technical difficulties. Please try again later.")