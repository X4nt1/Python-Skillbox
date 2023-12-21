import os
path = input("Введите путь до каталога: ")
size_catalog = 0
count_dirs = 0
count_files = 0
for i_file in os.listdir(path):
    size = os.path.getsize(i_file)
    size_catalog += size
    if os.path.isdir(i_file):
        count_dirs += 1
    elif os.path.isfile(i_file):
        count_files += 1
print(f'Размер каталога (в Кбайтах): {size_catalog/1024}')
print(f'Количество подкаталогов: {count_dirs}')
print(f'Количество файлов: {count_files}')
