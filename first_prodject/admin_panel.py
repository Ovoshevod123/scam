from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode
from reply import buttons, coin, admin_buttons
from inf import ADMIN_LIST
import sqlite3

rt_3 = Router()

class Edit(StatesGroup):
    #Шаги состояний
    name = State()
    edit = State()

@rt_3.message(Command('admin'))
async def admin(message: Message):
    rows = [[admin_buttons[0]]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    if message.from_user.id == ADMIN_LIST:
        await message.answer(text='Вы вошли в админ понель', reply_markup=markup)

@rt_3.callback_query(F.data == 'balance')
async def balance_1(message, state: FSMContext):
    await state.set_state(Edit.name)
    await message.message.edit_text(text='Введите никнейм пользователя\n'
                                         'Пример: @bobr (только без @)')

@rt_3.message(Edit.name)
async def balance_2(message: Message, state: FSMContext):
    rows = [[admin_buttons[1], admin_buttons[2]]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    db = sqlite3.connect('users.db')
    cur = db.cursor()
    a = cur.execute(f"SELECT balance FROM users WHERE text_id == {Edit.name}")
    print(a)
    await state.update_data(name=message.text)
    await message.answer(text='Что хотите сделать?', reply_markup=markup)
    await state.set_state(Edit.edit)


# @rt_3.message(Command('id'))
# async def id(message: Message):
#     await message.answer(text=f'{message.from_user.id}')