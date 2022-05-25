import os
import shutil
from datetime import datetime
import time

start_time = datetime.now()

PATH_PHONE = r"C:\Users\HP\python\агрегатор\photo_phone"
PATH_PC = r"C:\Users\HP\python\агрегатор\photo_PC"


def aggregator(path_phone: str, path_PC: str):
    dir_phone = os.listdir(path_phone) 
    for file in dir_phone:
        path_to_file = os.path.join(path_phone,file)                 
        if os.path.isfile(path_to_file):                             # проверяем является ли файлом
            shutil.copy(path_to_file, path_PC, follow_symlinks=True) # копируем на ПК
        else:
            new_path_PC = os.path.join(path_PC,file)                 # обновляем путь с учётом вложенности папок
            os.mkdir(new_path_PC)                                    # создаем папку на ПК
            new_path_phone = os.path.join(path_phone,file)           # новый путь для новой папки
            aggregator(new_path_phone, new_path_PC)                  # рекурсия с новыми путями

time.sleep(5)
print(datetime.now() - start_time)

def main():
    aggregator(path_PC=PATH_PC, path_phone=PATH_PHONE)

    
if __name__ == '__main__':
    main()