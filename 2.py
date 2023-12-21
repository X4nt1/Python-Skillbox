#1
import math
num = int(input("Введите число: "))
numbers = []
for i in range(1, num + 1, 2):
    numbers.append(i)

print("Список из нечётных чисел от одного до N: {numbers}")

#2
names = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
print("Первый день: {names[::2]}")

#3
cards_count = int(input("Количество видеокарт: "))
cards = []
last_cards = []

for i in range(cards_count):
    cards.append(int(input(f"Видеокарта {i + 1}: ")))

max_cards = max(cards)
for i in cards:
    if i != max_cards:
        last_cards.append(i)

print(f"Старый список видеокарт: {cards}")
print(f"Новый список видеокарт: {last_cards}")

#4
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favourites_count = int(input("Сколько фильмов хотите добавить? "))
favourites = []

for i in range(favourites_count):
    film = input("Введите название фильма: ")

    if film in films:
        favourites.append(film)
    else:
        print(f"Ошибка: фильма {film} у нас нет :(")

print(f"Ваш список любимых фильмов: {', '.join(favourites)}")

#5
conts_count = int(input("Количество контейнеров: "))
containers = []

for i in range(conts_count):
    weight = int(input("Введите вес контейнера: "))
    if weight > 200:
        print('Извините, вес контейнера слишком велик для данного склада')
    else:
        containers.append(weight)

new_cont_weight = int(input('Введите вес нового контейнера: '))
containers.append(new_cont_weight)
containers.sort(reverse=True)
print(containers)
print(f"Новый контейнер получит номер {containers.index(new_cont_weight)+1}")

#6
list = [1, 2, 3, 4, 5]
result=[]
shift = int(input("Сдвиг: "))

for i in range(-shift, len(list) - shift):
    result.append(list[i % len(list)]);

print(f"Изначальный список: {list}")
print(f"Сдвинутый список: {result}")

#7
word = input("Введите слово: ")
if word == word[::-1]:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

#8
def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

numbers_to_sort = [1, 4, -3, 0, 10]
print("Изначальный список:", numbers_to_sort)

bubble_sort(original_list)
print("Отсортированный список:", numbers_to_sort)

#9
numbers = [1.9, 2.6, 3.2, 4.5, 5.1]
numbers = [int(num) for num in numbers][::-1]

for i in range(-1, len(numbers) - 1, 1):
    if numbers[i] % 2 == 0:
        print(numbers[i], end=' ')
