#1
students = {
1: {
'name': 'Bob',
'surname': 'Vazovski',
'age': 23,
'interests': ['biology, swimming']
},
2: {
'name': 'Rob',
'surname': 'Stepanov',
'age': 24,
'interests': ['math', 'computer games', 'running']
},
3: {
'name': 'Alexander',
'surname': 'Krug',
'age': 22,
'interests': ['languages', 'health food']
}
}

def f(dict):
    lst = []
    cnt = 0
    for people in dict.values():
        lst += (people['interests'])
        cnt += len(people['surname'])
    return set(lst), cnt

pairs = []
for i, people in students.items():
    pair_tuple = (i, people['age'])
    pairs.append(pair_tuple)

my_lst, l = f(students)
print(f'Список пар «ID студента — возраст»: {pairs}')
print(f'Полный список интересов всех студентов: {my_lst}')
print(f'Общая длина всех фамилий студентов: {l}')

#2
def is_prime(num):
    if num < 2 : return False
    if num == 2 : return True
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True
def crypto(arr):
    return [count for i, count in enumerate(arr) if is_prime(i) ]
print(crypto('О Дивный Новый мир!'))

#3
players = {
("Ivan", "Volkin"): (10, 5, 13),
("Bob", "Robbin"): (7, 5, 14),
("Rob", "Bobbin"): (12, 8, 2)
}
players_points = [player + point for player,point in players.items()]
print(players_points)

#4
import random
orig_list = [random.randint(0,100) for _ in range(10)]
print(f'Оригинальный список: {orig_list}')
new_list = [(orig_list[i], orig_list[i+1]) for i in range(0,10,2)]
print(f'Новый список: {new_list}')
new_list_2 = list(zip([orig_list[i*2] for i in range(0,5)],[orig_list[i*2+1] for i in range(0,5)]))
print(f'Новый список 2: {new_list_2}')

#5
def tpl_sort(tpl):
    for num in tpl:
        if not isinstance(num, int):
            return tpl
    return tuple(sorted(tpl))
print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))

#6
tell_book = {}
while True:
    num = int(input('Введите номер действия:\n1. Добавить контакт.\n2. Найти человека.\n'))
    if num == 1:
        print('При выборе действия 1: ')
        people = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
        if people in tell_book:
            print('Такой человек уже есть в контактах.')
        else:
            num_tel = int(input('Введите номер телефона: '))
        tell_book[people] = num_tel
        print(f'Текущий словарь контактов: {tell_book}')
    elif num == 2:
        print('При выборе действия 2: ')
        surname = input('Введите фамилию для поиска: ')
        for people in tell_book:
            if surname in people:
                print(' '.join(people), tell_book[people])
    else:
        print('\nВведите коректную цифру\n')

#7
def my_zip(a,b):
    return ((a[i], b[i]) for i in range(min(len(a), len(b))))
str = 'abcd'
tpl = (10, 20, 30, 40)
res = my_zip(str,tpl)
print(my_zip(str,tpl))
for i in res:
    print(i)
