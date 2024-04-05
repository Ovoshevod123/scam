from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode
from reply import buttons, coin
import sqlite3

rt = Router()

async def new_def(message: Message):
    db = sqlite3.connect('users.db')
    cur = db.cursor()
    a = cur.fetchall()
    for i in range(len(a)):
        db = sqlite3.connect('users.db')
        cur = db.cursor()
        if a[i-1][0] != message.from_user.id:
            cur.execute(f"INSERT INTO users VALUES ('{message.from_user.id}', '{message.from_user.username}', '{message.from_user.full_name}', 0)")
            db.commit()
            db.close()
    await main(message)

async def main(message: Message):
    rows = [[buttons[0], buttons[1]],
            [buttons[2]],
            [buttons[3]],
            [buttons[5]]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    try:
        await message.message.edit_text(text='Здесь будет основная инфа о боте', reply_markup=markup)
    except:
        await message.answer(text='Здесь будет основная инфа о боте', reply_markup=markup)

async def top_def(message: Message):
    rows = [[buttons[6]]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.message.edit_text(text='Пополнение баланса \n\n'
                                         'Минимальная сумма: \n'
                                         '2000 RUB \n\n'
                                         'Введите сумму для пополнения', reply_markup=markup)

async def withdraw_def(message: Message):
    rows = [[buttons[6]]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.message.edit_text(text='Вывод средств \n\n'
                                         'Минимальная сумма вывода: \n'
                                         '2000 RUB \n\n'
                                         'Введите сумму для вывода', reply_markup=markup)

async def trading_def(message: Message):
    rows = [[coin[0], coin[1]],
            [buttons[6]]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.message.edit_text(text='Торговый счет \n\n'
                                         'Выберите монету для приобритения \n', reply_markup=markup)

async def support_def(message: Message):
    rows = [[buttons[4]],
            [buttons[6]]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.message.edit_text(text='Не приходят деньги? \n\n'
                                         'Иди поплач в поддержку \n', reply_markup=markup)

@rt.message(Command('start'))
async def new_1(message: Message):
    rows = [[buttons[7]]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(text='Здравсвуйте', reply_markup=markup)

@rt.callback_query(F.data == 'reg')
async def reg(message):
    await new_def(message)

@rt.callback_query(F.data == 'menu')
async def start_2(message: Message):
    await main(message)

@rt.callback_query(F.data == 'top')
async def top_1(message: Message):
    await top_def(message)

@rt.callback_query(F.data == 'withdraw')
async def withdraw_1(message: Message):
    await withdraw_def(message)

@rt.callback_query(F.data == 'trading')
async def trading_1(message: Message):
    await trading_def(message)

@rt.callback_query(F.data == 'support')
async def support_1(message: Message):
    await support_def(message)

# @rt.message(F.text.lower() == 'меню')
# async def start(message: Message):
#     await message.answer('menu', reply_markup=reply.start_kb2.as_markup(resize_keyboard=True))
#
# @rt.message(F.text.lower() == 'button 2')
# async def start(message: Message):
#     await message.answer('opros', reply_markup=reply.start_kb2.as_markup(resize_keyboard=True))
#
# class AddProduct(StatesGroup):
#     #Шаги состояний
#     name = State()
#     description = State()
#     price = State()
#     image = State()
#
# @rt.message(StateFilter(None), F.text == "Добавить товар")
# async def add_product(message: types.Message, state: FSMContext):
#     await message.answer(
#         "Введите название товара", reply_markup=types.ReplyKeyboardRemove()
#     )
#     await state.set_state(AddProduct.name)

@rt.callback_query(F.data == 'id')
async def call_text(callback: CallbackQuery):
    rows = [[buttons[3], buttons[4]],
            [buttons[5]],
            [buttons[2]]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await callback.answer('Ваш личный кабинет')
    await callback.message.edit_text(text=f'Ваш кабинет \nСчет: 0 RUB', reply_markup=markup)