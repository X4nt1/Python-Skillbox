#1
violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}
count = int(input('Сколько песен выбрать? '))
sum = 0
for i in range(1,count+1):
    name = input(f'Название {i}-й песни:')
    if name in violator_songs:
        sum += violator_songs[name]
print(f'Общее время звучания песен: {round(sum, 2)} минуты')

#2
data = {
"address": "0x544444444444",
"ETH": {
"balance": 444,
"totalIn": 444,
"totalOut": 4
},
"count_txs": 2,
"tokens": [
{
"fst_token_info": {
"address": "0x44444",
"name": "fdf",
"decimals": 0,
"symbol": "dsfdsf",
"total_supply": "3228562189",
"owner": "0x44444",
"last_updated": 1519022607901,
"issuances_count": 0,
"holders_count": 137528,
"price": False
},
"balance": 5000,
"totalIn": 0,
"total_out": 0
},
{
"sec_token_info": {
"address": "0x44444",
"name": "ggg",
"decimals": "2",
"symbol": "fff",
"total_supply": "250000000000",
"owner": "0x44444",
"last_updated": 1520452201,
"issuances_count": 0,
"holders_count": 20707,
"price": False
},
"balance": 500,
"totalIn": 0,
"total_out": 0
}
]
}
print(data.keys(), data.values())
data['ETH']['total_dif'] = 100
data["tokens"][0]['fst_token_info']['name'] = 'doge'
data['ETH']['totalOut'] = data["tokens"][0].pop('total_out') + data["tokens"][1].pop('total_out')
data["tokens"][1]['sec_token_info']['total_price'] = data["tokens"][1]['sec_token_info'].pop('price')

#3
goods = {
'Лампа': '12345',
'Стол': '23456',
'Диван': '34567',
'Стул': '45678',
}
store = {
'12345': [
{'quantity': 27, 'price': 42},
],
'23456': [
{'quantity': 22, 'price': 510},
{'quantity': 32, 'price': 520},
],
'34567': [
{'quantity': 2, 'price': 1200},
{'quantity': 1, 'price': 1150},
],
'45678': [
{'quantity': 50, 'price': 100},
{'quantity': 12, 'price': 95},
{'quantity': 43, 'price': 97},
],
}
def found_summ_count(good):
    count = 0
    sum = 0
    for form in store[good]:
        count += form['quantity']
        sum += form['quantity'] * form['price']
    return count, sum
for good in goods:
    if goods[good] in store:
        count, sum = found_summ_count(goods[good])
    print(f'{good} — {count} штук, стоимость {sum} руб.')

#4
def print_dict(text,dict):
    print(text)
    for item in dict:
        print(item,':',dict[item])


text = input('Введите текст: ')
frequency = {}
for let in text:
    if let in frequency:
        frequency[let] +=1
    else:
        frequency[let] = 1
frequency_reverse = {}
for let in frequency:
    value = frequency[let]
    if value in frequency_reverse:
        frequency_reverse[value].append(let)
    else:
        frequency_reverse[value] = [let]
print_dict('\nОригинальный словарь частот:\n', frequency)
print_dict('\nИнвертированный словарь частот:\n', frequency_reverse)

#5
count = int(input('Введите количество пар слов: '))
synonyms = {}
for i in range(count):
    pair = input(f'{i + 1}-ая пара: ')
    pair_list = pair.split('-')
    synonyms[pair_list[0]] = pair_list[1]
while True:
    word = input('Введите слово: ')
    for key, value in synonyms.items():
        if key.lower() == word.lower():
            print('Синоним:', value)
            break
        elif value.lower() == word.lower():
            print('Синоним:', key)
            break
    else:
        print('Такого слова в словаре нет.')

#6
count = int(input('Введите количество заказов: '))
salespeople = {}
for i in range(1, count + 1):
    order = input(f'{i}-ый заказ: ').split()
    if order[0] in salespeople:
        salespeople[order[0]][i] = f'{order[1]}:{order[2]}'
    else:
        salespeople[order[0]] = {i: f'{order[1]}: {order[2]}'}
sorted_salespeople = dict(sorted(salespeople.items()))
for name in sorted_salespeople:
    print(f'{name}:')
    for i in sorted_salespeople[name]:
        print(sorted_salespeople[name][i])

#7
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
print('Задача 1:')
print('Решение без множеств:', end = '')
for num in sorted([num for num in array_1 if num in array_2 and num in array_3]):
    print(num, end = " ")
print('\nРешение с множествами:', end = '')
for num in sorted(set(array_1) & set(array_2) & set(array_3)):
    print(num, end = " ")
print('\nЗадача 2:')
print('Решение без множеств:', end = '')
for num in sorted([num for num in array_1 if not(num in array_2 or num in array_3)]):
    print(num, end = " ")
print('\nРешение с множествами:', end = '')
for num in sorted(set(array_1) - set(array_2) - set(array_3)):
    print(num, end = " ")
