from aiogram import Bot
import os #для работы с файлами

async def save_photo(bot:Bot,photo,user_id:int): #функция в которой есть бот,фото,юзер инт нужен потомучто юзер пользователя состоит из цифр всегда
    # print(f'сохраняю {user_id}')
    # return 'memories/my_photo.jpg',500
    file = await bot.get_file(photo.file_id) #получаем информацию о фото
    print(f'файл: {file.file_path}')
    file_jpg = '.jpg' #фотки всегда jpg это расширение фотки
    file_nam = f'photo_{user_id}_{photo.file_id}_{file_jpg}' #это имя файла уникальное потомучто в нем есть юникальные цифры пользователя и информацию о фотке в режиме jpg
    file_path = f'memories/{file_nam}' #путь в котором будет попадать фото
    await bot.download_file(file.file_path, file_path) #скачиваем фото с серверов тг и в нем же и храниться путь к файлу на сервере тг и куда будет сохраняться это фото на твой пк
    file_bait = os.path.getsize(file_path) #возвращает размер файла в байтах
    print(f'успех_{file_path}_{file_path},байт')
    return file_path,file_bait,'photo','photo.jpg' #и возвращаем эти переменные для того чтобы их использовать в file.py


async def save_file(bot:Bot,Document,user_id:int):
    file = await bot.get_file(Document.file_id)
    print(f'файл: {file.file_path}')
    file1 = os.path.splitext(Document.file_name)[1]
    file_name = f'Document_{user_id}_{Document.file_id}_{file1}'
    file_path = f'memories/{file_name}'
    await bot.download_file(file.file_path,file_path)
    file_doc = os.path.getsize(file_path)
    print(f'успех_{file_path}_{file_path},документ')
    return file_path,file_doc,'file',Document.file_name