len_strs = 0
count = 0

with open('people.txt', 'r', encoding = 'utf-8') as people_file:
    for i_line in people_file:
        count += 1
        length = len(i_line)
        if i_line.endswith('\n'):
            length -= 1
        len_strs += length
        try:
            if length < 3:
                raise BaseException()
        except BaseException:
            print(f'Ошибка: менее трёх символов в строке {count}.')
print(f'Общее количество символов: {len_strs}.')
