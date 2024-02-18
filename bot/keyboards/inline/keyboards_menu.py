from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# menu = ReplyKeyboardMarkup(resize_keyboard=True).row(
#             KeyboardButton("/start"),  #TODO kind of "leave your mail or number button. Or our contacts"
#             KeyboardButton("/exit")
# )

inline_kb = InlineKeyboardMarkup(resize_keyboard=True).add(
            InlineKeyboardButton(text="Issue 1", callback_data="Issue1"),
            InlineKeyboardButton(text="Issue 2", callback_data="Issue2"),
            InlineKeyboardButton(text="Issue 3", callback_data="Issue3"),
            InlineKeyboardButton(text="Issue 4", callback_data="Issue4")
)