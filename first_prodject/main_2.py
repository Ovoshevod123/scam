import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from hand import rt
from reply import rt_2
from admin_panel import rt_3
from bot_cmds import private
from inf import TOKEN, ADMIN_LIST

BOT_TOKEN = TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
dp.include_routers(rt, rt_2, rt_3)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

asyncio.run(main())