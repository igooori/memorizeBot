from aiogram import Router,F,Bot
from aiogram.types import Message
from utils.file_server import save_file #иппорт функции из другого файла
from models.memory import save

router = Router()

@router.message(F.document) #фильтрует сообщения только с документами
async def docum(message:Message,bot:Bot): #функция
    document = message.document #ловит файл пользователя с документом
    await message.answer(f'Файл {document} получен 📁') #оповещаем пользователя что его файл получен
    file_path,file_doc,file_type,original_name = await save_file(bot,document,message.from_user.id) #это название переменных из другого файла и функция из другого файла
    print(f'сохранено {file_path}') #для себя чтобы в команде убедиться что все работает
    await message.answer(f'Документ получен! {document.file_name}')
    save(
        user_id=message.from_user.id,
        file_path=file_path,
        file_bait=file_doc,
        file_type=file_type,
        original_name=original_name,
        
    ) #это переменные из файла с бд и так называються переменные с бд
    await message.answer('ваши документы сохранены!')