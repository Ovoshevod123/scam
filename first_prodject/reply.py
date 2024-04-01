from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove, \
    KeyboardButtonPollType, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery
from aiogram import F, Router

rt_2 = Router()

top = InlineKeyboardButton(text='Пополнение', callback_data='top')
withdraw = InlineKeyboardButton(text='Вывод', callback_data='withdraw')
currency = InlineKeyboardButton(text='Настройка валюты', callback_data='currency')
button4 = InlineKeyboardButton(text='f', callback_data='f')
button5 = InlineKeyboardButton(text='g', callback_data='g')
id = InlineKeyboardButton(text='Личный кабинет', callback_data='id')
course = InlineKeyboardButton(text='Курс валют', callback_data='course')
button_back = InlineKeyboardButton(text='Главное меню', callback_data='menu')
buttons = [id, course, button_back, top, withdraw, currency, button5]

# start_kb = ReplyKeyboardBuilder()
# start_kb.add(
#     KeyboardButton(text='меню'),
#     KeyboardButton(text='Добавить товар')
# )
# start_kb.adjust(2)
#
# start_kb2 = ReplyKeyboardBuilder()
# start_kb2.attach(start_kb)
# start_kb2.row(KeyboardButton(text='Button 3'))

del_kb = ReplyKeyboardRemove()
