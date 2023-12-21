from people_house import People,House
count_day = 0
house = House()
people_1 = People('Misha', house)
people_2 = People('Egor', house)
while count_day < 365 and people_1.alive and people_2.alive:
    count_day += 1
    print(f'День {count_day}')
    people_1.live()
    people_2.live()
if count_day == 365:
    print(f'{people_1.name} и {people_2.name} прожили год без потерь')
elif not people_1.alive:
    print(f'Умер {people_1.name} на {count_day} день')
elif not people_2.alive:
    print(f'Умер {people_2.name} на {count_day} день')
else:
    print(f'Умерли оба на {count_day} день')

