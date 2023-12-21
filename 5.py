#1
menu = input('Доступное меню: ')
print('Сейчас в меню есть:', ', '.join(menu.split(';')))

#2
str = input('Введите строку: ').split()
str_list =[len(word) for word in str]
max_word = str[str_list.index(max(str_list))]
print('Самое длинное слово:', max_word)
print('Длина этого слова:', len(max_word))

#3
name = input('Название файла: ')
ban_let = ['@', '№', '$', '%', '^', '&', '*']
if name.startswith('@№$%^*()'):
    print('Ошибка: название начинается недопустимым символом.')
elif name.endswith('.txt') or name.endswith('.docx'):
    print('Файл назван верно.')
else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')

#4
print(' '.join(w.lower().capitalize() for w in input('Введите строку: ').split()))

#5
password = input('Придумайте пароль: ')
up_let = [let for let in password if let.isupper()]
num = [let for let in password if let.isalpha()]
if len(password) > 7 and len(up_let) > 0 and len(num) > 2:
    print('Это надёжный пароль.')
else:
    print('Пароль ненадёжный. Попробуйте ещё раз.')

#6
text = input('Введите строку: ')
count = 1
for i in range(len(text)):
    if i == len(text)-1:
        print(text[i], end = '')
        print(count, end = '')
    elif text[i] == text[i+1]:
        count += 1
    else:
        print(text[i], end = '')
        print(count, end = '')
        count = 1

#7
ip = input('Введите IP: ').split('.')
for num in ip:
    if num.isdigit():
        if int(num) > 255:
            print('{0} превышает 255.'.format(num))
            break
        elif int(num) < 0:
            print('{0} меньше 0.'.format(num))
            break
    elif num.isalnum():
        print('{0} — это не целое число.'.format(num))
        break
    else:
        print('Адрес — это четыре числа, разделённые точками.')
        break
else:
    print('IP-адрес корректен.')

#8


#9
def count_uppercase_lowercase(text):
    up_let = [let for let in text if let.isupper()]
    low_let = [let for let in text if let.islower()]
    return len(up_let), len(low_let)
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)



