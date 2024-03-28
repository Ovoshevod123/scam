from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import F, Router

rt = Router

button1 = InlineKeyboardButton(text='a', callback_data='a')
button2 = InlineKeyboardButton(text='s', callback_data='s')
button3 = InlineKeyboardButton(text='d', callback_data='d')
button4 = InlineKeyboardButton(text='f', callback_data='f')
button5 = InlineKeyboardButton(text='g', callback_data='g')
button_back = InlineKeyboardButton(text='Назад', callback_data='back')
buttons = [button1, button2, button3, button4, button5, button_back]

@rt.callback_data(F.data == 'a')
async def callback_a():
    await callback_query.answer

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