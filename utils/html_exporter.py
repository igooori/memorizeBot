import os
from datetime import datetime #импорт времени
from models.memory import Memori
def html(user_id:int,memories:list) -> str: #это функция принимает id пользователя memories принмает список файлов из бд и str это возвращает в готовый html код
    html_number = [] #создаем перменную чтобы по частям собирать html код

    html_number.append("""<!DOCTYPE html>
<html>
<head><title>Мои воспоминания</title></head>
<body>
<h1>Мои воспоминания</h1>""") #html код
    for i,memory in enumerate(memories): #цикл который мемори в мемориес складывает все
        file = f'files/{i}_{memory.original_name}'
        if memory.type == 'photo': #проверяем фото это
            html_number.append(f"""
<div class='memory'>
<img src='{file}' alt='Фото'>
<p> название: {memory.original_name}</p>
</div> 
""") #html код
        else: #это уже для файла
            html_number.append(f"""
<div class='memory'>
<a href='{file}'</a>
<p>Название: {memory.original_name}</p>
</div>
""")
    html_number.append('</body></html>')
    return "\n".join(html_number) #возвращаем переменную html_number чтобы использовать ее
    