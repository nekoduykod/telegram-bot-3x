import logging
import json

import openai

from main import bot, dp, types
from aiogram.dispatcher import FSMContext
from bot.data.config import OPENAI_API_KEY


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# below - for direct gpt question
@dp.message_handler(commands=["gpt_request"])
async def gpt_request_command(message: types.Message):
    await message.answer("Please describe your question.")


@dp.message_handler(lambda message: message.text and not message.text.startswith('/'))
async def process_gpt_request_description(message: types.Message):
    request_text = message.text.strip()
    await send_direct_gpt_request(request_text, message.from_user.id)

async def send_direct_gpt_request(request_text: str, user_id: int):
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