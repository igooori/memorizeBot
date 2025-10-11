import zipfile
import os
import logging
from pathlib import Path
from utils.html_exporter import html as html_zip

def zip_archive(user_id:int,memories:list) -> str:
      zip_fil = f'temp/memories_{user_id}.zip'
      with zipfile.ZipFile(zip_fil, 'w') as zipf:
         zipf.writestr('test.txt','это документ')
         print('txt добавлен')
         for i ,memor in enumerate(memories):
            zipf.write(
               memor.file_path,
               f'files/{i}_{memor.original_name}'
            )
            print('добавлено имя файла')
         if memories:
            html_f = html_zip(user_id,memories)
            zipf.writestr(f'memories_{user_id}.html',html_f)
            print('добавлен html_f')
         return zip_fil