first_file = open('first_tour.txt', 'r', encoding='utf-8')
count_point = int(first_file.readline())
peoples = {}
for people in first_file:
    people_list = people.split()
    people_point = int(people_list[2])
    if people_point > 80:
        new_name = f'{people_list[1][0]}. {people_list[0]}'
        peoples[new_name] = people_point
first_file.close()
second_file = open('second_tour.txt', 'w')
sorted_peoples = sorted(peoples.items(), key= lambda item: item[1], reverse = True)
for i in enumerate(sorted_peoples):
    num = i[0]+1
    tpl = i[1]
    second_file.write(f'{num}) {tpl[0]} {tpl[1]}\n')
second_file.close()


        

