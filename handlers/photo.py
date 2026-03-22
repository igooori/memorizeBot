from aiogram import Router,F,Bot
from aiogram.types import Message
from utils.file_server import save_photo

from models.memory import save

router = Router()

@router.message(F.photo)
async def photo(message:Message,bot:Bot):
    photo = message.photo[-1]
    file_path,file_bait,file_type,original_name = await save_photo(bot,photo, message.from_user.id) 
    print(f'сохранено {file_path}')
    await message.answer('Фото получено! 📸')
    save(
        user_id=message.from_user.id,
        file_path=file_path,
        file_bait=file_bait,
        file_type=file_type,
        original_name=original_name,
    )
    await message.answer('ваше фото сохранено')
