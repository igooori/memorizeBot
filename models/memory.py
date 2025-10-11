from datetime import datetime #это нужно для времени
from sqlalchemy.orm import DeclarativeBase,Session #ипмортируем slqalchemy.orm и импортируем Session чтобы добавлять данные в бд
from sqlalchemy import Column,Integer,String,ForeignKey,create_engine,DateTime,JSON
engine =  create_engine('sqlite:///memory.db') #путь к файлу бд
class Base(DeclarativeBase): pass
class Memori(Base): #название бд
    __tablename__ = 'memories'
    #это название перменных которые обозначают id= чтобы было 1,2,3 и тд,user_id это там будет храниться user_id из тг,type там будет храниться фото\файл
    #file_patch хранит путь к файлу на пк,original_name там имя файла,file_size хранит сколько весит в байтах,created_at время когда файл был загружен
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer)
    type = Column(String)
    file_path = Column(String)
    original_name = Column(String)
    file_size = Column(Integer)
    created_at = Column(DateTime)
    tags = Column(JSON)
Base.metadata.create_all(bind=engine)

# with Session(bind=engine) as db:
#     db.query(Memori).delete() 
#     db.commit()
def save(user_id,file_path,file_bait,file_type,original_name): #cюда добавляем все перменные
    print(f'сохраняю в бд {original_name}')
    with Session(bind=engine) as db: #открываем session для сохранения данный
        new_memory_photo = Memori(user_id=user_id,
                                file_path=file_path,
                                file_size=file_bait,
                                type=file_type,
                                original_name=original_name,
                                created_at=datetime.now(),
                                tags=[])
        db.add(new_memory_photo) #это добавления данных в бд
        db.commit() #это сохранния всего что сделали в бд
