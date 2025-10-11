import asyncio  #для асинхроности бота
from aiogram import Bot,Dispatcher #импорты aiogram
from config import TOCEN #импорт токен бота из другого файла для того чтобы небыло видно токена
from aiogram.fsm.storage.memory import MemoryStorage #фсм нужен для состояний пользователя
from handlers.commands import router as router_commands #роутеры.импорты с другого файла чтобы бота появился команды потомучто мы запускаем через main
from handlers.photo import router as router_photo
from handlers.file import router as router_file

bot = Bot(token=TOCEN) #токе бота
dp = Dispatcher(storage=MemoryStorage()) #диспетчер

async def main():
    dp.include_router(router_commands)
    dp.include_router(router_photo)
    dp.include_router(router_file)
    await dp.start_polling(bot)
asyncio.run(main())