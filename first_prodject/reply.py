from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove, \
    KeyboardButtonPollType, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery
from aiogram import F, Router

rt_2 = Router()

top = InlineKeyboardButton(text='Пополнение', callback_data='top')
withdraw = InlineKeyboardButton(text='Вывод', callback_data='withdraw')
trading = InlineKeyboardButton(text='Торги', callback_data='trading')
support = InlineKeyboardButton(text='Техническая поддержка', callback_data='support')
support_2 = InlineKeyboardButton(text='Техническая поддержка', url='https://t.me/Kukuru3a', callback_data='support_2')
setting = InlineKeyboardButton(text='Настройки', callback_data='setting')

currency = InlineKeyboardButton(text='Настройка валюты', callback_data='currency')

new = InlineKeyboardButton(text='Регестрация', callback_data='reg')

btc = InlineKeyboardButton(text='Bitcoin', callback_data='btc')
eth = InlineKeyboardButton(text='Ethereum', callback_data='etc')

button_back = InlineKeyboardButton(text='Главное меню', callback_data='menu')
buttons = [top, withdraw, trading, support, support_2, setting, button_back, new]
coin = [btc, eth]

balance = InlineKeyboardButton(text='Настроить баланс пользователя', callback_data='balance')
balance_plus = InlineKeyboardButton(text='Увеличить баланс', callback_data='balance+')
balance_minus = InlineKeyboardButton(text='Уменьшить баланс', callback_data='balance-')
admin_buttons = [balance, balance_plus, balance_minus]

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
