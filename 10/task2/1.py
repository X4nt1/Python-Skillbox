import random
sum_num = 0
try:
    with open('out_file.txt', 'w') as res:
        while sum_num < 777:
            num = int(input('Введите число: '))
            if random.randrange(0,13) == 0:
                raise BaseException()
            sum_num += num
            res.write(f'{num}\n')
except BaseException:
    print('Вас постигла неудача!')
finally:
    print('Содержимое файла out_file.txt:')
    with open('out_file.txt', 'r') as res:
        for i_res in res:
            print(i_res[:-1])



