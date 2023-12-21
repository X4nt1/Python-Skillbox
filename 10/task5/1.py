import math
def squarte(num):
    try:
        res =math.sqrt(num)
        return res
    except ValueError:
        print('Число не может быть отрицательным')
        return None
    except Exception as exc:
        print(exc)
        return None
num = float(input('Введите число: '))
res = squarte(num)
if res != None:
    print(f'Результат: {res}')


