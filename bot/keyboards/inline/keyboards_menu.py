from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# menu = ReplyKeyboardMarkup(resize_keyboard=True).row(
#             KeyboardButton("/start"),  #TODO kind of "leave your mail or number button. Or our contacts"
#             KeyboardButton("/exit")
# )

builder = InlineKeyboardBuilder()
builder.add(InlineKeyboardButton(text="Issue 1", callback_data="Issue1"))
builder.adjust(1)  # Arrange buttons in 2 columns

inline_kb = builder.as_markup()