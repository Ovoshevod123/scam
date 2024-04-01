from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode
from reply import buttons

rt = Router()

class Form(StatesGroup):
    menu = State()
    id = State()
    currency = State()

async def main(message: Message):
    rows = [[buttons[0], buttons[1]]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    try:
        await message.message.edit_text(text='Здесь будет основная инфа о боте', reply_markup=markup)
    except:
        await message.answer(text='Здесь будет основная инфа о боте', reply_markup=markup)

@rt.message(Command('start'))
async def start(message: Message):
    await main(message)

@rt.callback_query(F.data == 'menu')
async def start_2(message: Message):
    await main(message)

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

@rt.message(F.text)
async def text(message:Message):
    await message.answer('it`s text')
