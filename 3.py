1
first_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]

merged_list = first + second
print(f"Количество цифр 5 при первом объединении: {merged_list.count(5)}")
merged_list = [i for i in merged_list if i != 5] + third_list
print(f"Количество цифр 3 при втором объединении: {merged_list.count(3)}")
print(f"Итоговый список: {merged_list}")

2
def merge_sorted_lists(list1, list2):
    return sorted(set(list1+list2))


merged_list = merge_sorted_lists([1, 3, 5, 7, 9], [2, 4, 5, 6, 8, 10])
print(merged_list)

3
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
shop_dictionary = {}

for i in shop:
    if i[0] in shop_dictionary:
        shop_dictionary[i[0]].append(i[1])
    else:
        shop_dictionary[i[0]] = [i[1]]

detail = input("Название детали: ")

if detail in shop_dictionary:
    print(f"Количество деталей: {len(shop_dictionary[detail])}")
    print(f"Общая стоимость: {sum(shop_dictionary[detail])}")
else:
    print("Такой детали нет на складе")

4
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
valuable_cases = ['пришёл', 'ушёл', 'пора спать']

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")

    case = input("Гость пришёл или ушёл?").lower()

    if case == 'пора спать':
        print("Вечеринка закончилась, все легли спать")
        break
    elif case not in valuable_cases:
        print("Ответьте на вопрос, либо напишите 'пора спать'\n")
        continue

    name = input("Имя гостя: ")

    if case == 'пришёл':
        if len(guests) < 6:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет")
    elif case == 'ушёл':
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")
        else:
            print(f"{name} не был(а) на вечеринке")

5
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

playTime = 0.0
for i in range(int(input("Сколько песен выбрать?"))):
    song = input(f"Название {i + 1}-й песни: ")
    for i in violator_songs:
        if song == i[0]:
            playTime += i[1]
print(f"Общее время звучания песен — {playTime} минуты")

6
def find_max_pairs(roller_sizes, people_sizes, pairs_count=0):

    for size in people_sizes:
        for rollers in rollers_sizes:
            if rollers_sizes[roller_sizes.index(rollers)] == size:
                pairs_count += 1
                continue

    return pairs_count


rollers_count = int(input("Количество роликов: "))
rollers_sizes = [int(input(f"Размер пары {i + 1}: ")) for i in range(rollers_count)]

people_count = int(input("\nКоличество людей: "))
people_sizes = [int(input(f"Размер ноги человека {i + 1}: ")) for i in range(people_count)]

result = find_max_pairs(rollers_sizes, people_sizes)

print(f"\nНаибольшее количество людей, которые могут взять ролики: {result}")

7
humans = [i + 1 for i in range(int(input("Количество человек: ")))]
shift = int(input("Какое число в считалке?"))
index = 0

while len(humans) > 1:
    print(f"\nТекущий круг людей: {humans}\n"
          f"Начало счёта с номера {humans[index]}")
    retired_index = (index + shift - 1) % len(humans)
    print(f"Выбывает человек под номером {humans[retired_index]}")
    humans.remove(humans[retired_index])
    index = retired_index % len(humans)

print(f"\nОстался человек под номером {humans[0]}")

#8
def is_palindrome(numbers: list, start_index: int) -> bool:
    for i in range((len(numbers) - start_index) // 2):
        if numbers[start_index + i] != numbers[-(i + 1)]:
            return False
    return True


sequence = [int(input("Число: ")) for _ in range(int(input("Количество чисел: ")))]

for i in range(len(sequence)):
    if is_palindrome(sequence, i):
        print(f"Нужно приписать чисел: {i}")
        print(f"Сами числа: {sequence[i - 1::-1]}")
        break
