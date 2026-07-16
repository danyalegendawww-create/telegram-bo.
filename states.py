from aiogram.fsm.state import State, StatesGroup


class BuyState(StatesGroup):
    waiting_for_nickname = State()
