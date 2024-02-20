from aiogram.fsm.state import State, StatesGroup


class ChooseButton(StatesGroup):
    Issues = State()

class Issue1Form(StatesGroup):
    Item1 = State()
    Item1_comment = State()

class LeavePhoto(StatesGroup):
    URL = State()
    URL_processing = State()