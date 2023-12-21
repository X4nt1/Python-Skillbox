1
def found_vowels(text):
    vowels = [x for x in text if (x.lower() == 'о') or (x.lower() == 'а') or (x.lower() == 'у') or (x.lower() == 'я'
            or (x.lower() == 'е') or (x.lower() == 'ю') or (x.lower() == 'ё'))]
    return vowels
text = input('Введите текст: ')
res = found_vowels(text)
print('Список гласных букв:', res)
print('Длина списка:', len(res))

#2
count = int(input('Введите длину списка: '))
res = [1 if x % 2 == 0 else x % 5 for x in range(0,count)]
print('Результат:',  res)

#3
import random
team1 = [random.randrange(500,1001)/ 100 for _ in range(20)]
team2 = [random.randrange(500,1001)/ 100 for _ in range(20)]
win = [team1[i] if team1[i] > team2[i] else team2[i] for i in range(20)]
print('Первая команда:', team1)
print('Вторая команда:', team2)
print('Победители тура:', win)

#4
alphabet = 'abcdefg'
print('1:', alphabet[:])
print('2:', alphabet[::-1])
print('3:', alphabet[::2])
print('4:', alphabet[1::2])
print('5:', alphabet[:1])
print('6:', alphabet[:-2:-1])
print('7:', alphabet[3:4])
print('8:', alphabet[-3:])
print('9:', alphabet[3:5])
print('10:', alphabet[4:2:-1])

#5
str = input('Введите строку: ')
first_h = str.index('h')
last_h = str.rindex('h')
print('Развёрнутая последовательность между первым и последним h:', str[last_h-1:first_h:-1])

#6
print([[x+i*2 for i in range(3)] for x in range(1,5)])

#7
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print([z for x in nice_list for y in x for z in y])

#8
text = input('Введите сообщение: ')
shiwt = int(input('Введите сдвиг: '))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
res = [
    [alphabet[alphabet.index(let) + shiwt]
       if alphabet.index(let) + shiwt < 33
       else alphabet[((alphabet.index(let) + shiwt) % 32) -1]]
       if let != ' ' else ' '
       for let in text]
print(''.join([i for c in res for i in c]))