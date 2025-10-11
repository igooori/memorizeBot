from aiogram import Router #роутер
from aiogram.types  import Message,InlineKeyboardButton,InlineKeyboardMarkup #инлаин кнопки и message
from aiogram.filters import Command #для создания команд
import os #для работы с файлами?
from sqlalchemy.orm import Session #для работы с sqlalchemy и импорт Session
from utils.zip_archiver import zip_archive #путь к файлу и импортируем функцию из файла
from sqlalchemy import create_engine
from models.memory import Memori #импорт бд 
from aiogram.types import BufferedInputFile
router = Router()

@router.message(Command('start')) #команда старт для запуска бота
async def start(message:Message):
    await message.answer('Привет! Отправляй мне фото или файлы — я сохраню их как твои воспоминания. Используй /search для поиска и /export для экспорта всего архива.')#сообщение пользователю
@router.message(Command('help'))
async def help(message:Message):
    await message.answer('Отправь фото или файл. Используй /search <слово> для поиска по имени файла. /export — экспортировать полный архив в ZIP.')
@router.message(Command('search')) #для поиска фото/файла
async def search(message:Message):
    text = message.text.split(maxsplit=1)
    searc = text[1].strip()
    engine = create_engine('sqlite:///memory.db')
    with Session(bind=engine) as db:
        memori = db.query(Memori).filter(Memori.user_id == message.from_user.id,
                                 Memori.original_name.ilike(f'%{searc}%')
                                 ).order_by(Memori.created_at.desc()).all()
    poisk = f'нашел{len(memori)}'
    for i,memor in enumerate(memori,1):
        if memor.type == 'photo':
            poisk += f'{i} {memor.original_name}'
        else:
            poisk += f'{i} {memor.original_name}'
    await message.answer(poisk)

@router.message(Command('export'))
async def export(message:Message):
    engine = create_engine('sqlite:///memory.db')
    with Session(bind=engine) as db:
        memories = db.query(Memori).filter(
            Memori.user_id == message.from_user.id
        ).all()

    zip_fl = zip_archive(message.from_user.id,memories)
    with open(zip_fl,'rb') as f:
        zip_data = f.read()
    document = BufferedInputFile(zip_data,filename='memories_arh.zip')
    await message.answer_document(document=document,caption='ваш архив')
    os.remove(zip_fl)
    await message.answer('все рахив создан')