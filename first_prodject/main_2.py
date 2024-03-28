import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from first_prodject.hand import rt
from first_prodject.bot_cmds import private

BOT_TOKEN = '6717750681:AAE6J3N7i9IftrOAeZWbPdLTkDeALQRI1s8'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
dp.include_router(rt)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

asyncio.run(main())