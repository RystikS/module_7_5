import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(directory, file)
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(directory)
    parent_dir = os.path.dirname(directory)
    print(f'Обнаружен файл: {file},'
          f' Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, '
          f'Родительская директория: {parent_dir}')
