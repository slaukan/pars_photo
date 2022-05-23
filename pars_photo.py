import os
import shutil
from datetime import datetime
import time

start_time = datetime.now()

tek_dir = os.getcwd() # Текущая деректория:
print(tek_dir)
dir = 'фото_1'        # папка откуда копируем фото
dir2 = 'фото_2'       # папка куда копируем

# pa=os.listdir('C:\Users\HP\python\агрегатор\фото 1')
# print(pa)

for dirpath, dirs, files in os.walk(os.path.join(tek_dir)):
    for file in files:
        shutil.copy(dirpath+"\\"+file, dir2, follow_symlinks=True)  # каждый абсолютный путь файла переносим в папку фото_2
# set_photo = set(files)
    
time.sleep(5)

print(datetime.now() - start_time)
# for _, _, files in os.walk(os.path.join(dir2)):
#     set_photo_2 = set(dir2)
# print(set_photo)
# print(set_photo_2)